"""
helloworld.core
===============

Greeting orchestration runtime.

This module implements the middleware-chain orchestrator that sits between
the plugin registry, the feature flag provider, the telemetry pipeline, and
the character emitter.
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys
import time
import uuid
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from enum import Enum
from typing import (
    Any, AsyncIterator, Awaitable, Callable, Mapping, Protocol, TypedDict,
    runtime_checkable,
)

from .feature_flags import (
    ChainedFeatureFlagProvider, EnvironmentFeatureFlagProvider,
    FeatureFlagProvider,
)
from .metrics import MetricsRegistry, serve_metrics
from .plugins import GreeterPlugin, PluginRegistry

logger = logging.getLogger("helloworld.core")


# ---------------------------------------------------------------------------
# Typed telemetry payloads
# ---------------------------------------------------------------------------

class GreetingStartedPayload(TypedDict):
    correlation_id: str
    locale: str
    plugin: str


class GreetingCompletedPayload(TypedDict):
    correlation_id: str
    characters_emitted: int
    duration_seconds: float


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

class OutputSink(str, Enum):
    STDOUT = "stdout"
    STDERR = "stderr"


@dataclass(frozen=True)
class GreetingConfig:
    locale: str = "en-GB"
    plugin: str = "default"
    sink: OutputSink = OutputSink.STDOUT
    terminator: str = "\n"
    enable_health: bool = False
    enable_metrics: bool = False
    health_port: int = 8080
    metrics_port: int = 9090

    @classmethod
    def from_environment(cls) -> "GreetingConfig":
        return cls(
            locale=os.environ.get("HELLOWORLD_LOCALE", "en-GB"),
            plugin=os.environ.get("HELLOWORLD_PLUGIN", "default"),
            sink=OutputSink(os.environ.get("HELLOWORLD_SINK", "stdout")),
            terminator=os.environ.get("HELLOWORLD_TERMINATOR", "\n"),
            enable_health=_env_bool("HELLOWORLD_ENABLE_HEALTH", False),
            enable_metrics=_env_bool("HELLOWORLD_ENABLE_METRICS", False),
            health_port=int(os.environ.get("HELLOWORLD_HEALTH_PORT", "8080")),
            metrics_port=int(os.environ.get("HELLOWORLD_METRICS_PORT", "9090")),
        )


def _env_bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


# ---------------------------------------------------------------------------
# Telemetry
# ---------------------------------------------------------------------------

@runtime_checkable
class TelemetryReporter(Protocol):
    def report(self, event: str, payload: Mapping[str, Any]) -> None: ...


class LoggingTelemetryReporter:
    def report(self, event: str, payload: Mapping[str, Any]) -> None:
        logger.info("TELEMETRY event=%s payload=%s", event, dict(payload))


# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------

@dataclass
class GreetingContext:
    correlation_id: str
    locale: str
    plugin_name: str
    message: str = ""
    characters_emitted: int = 0
    started_at: float = field(default_factory=time.perf_counter)


Middleware = Callable[
    [GreetingContext, Callable[[GreetingContext], Awaitable[None]]],
    Awaitable[None],
]


async def correlation_middleware(
    ctx: GreetingContext, call_next: Callable[[GreetingContext], Awaitable[None]]
) -> None:
    logger.debug("[%s] entering pipeline", ctx.correlation_id)
    await call_next(ctx)
    logger.debug("[%s] pipeline complete", ctx.correlation_id)


async def timing_middleware(
    ctx: GreetingContext, call_next: Callable[[GreetingContext], Awaitable[None]]
) -> None:
    start = time.perf_counter()
    try:
        await call_next(ctx)
    finally:
        elapsed = time.perf_counter() - start
        logger.debug("[%s] pipeline took %.6fs", ctx.correlation_id, elapsed)


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

class GreetingOrchestrator:
    def __init__(
        self,
        config: GreetingConfig,
        plugins: PluginRegistry,
        flags: FeatureFlagProvider,
        metrics: MetricsRegistry,
        telemetry: TelemetryReporter,
        middleware: list[Middleware] | None = None,
    ) -> None:
        self._config = config
        self._plugins = plugins
        self._flags = flags
        self._metrics = metrics
        self._telemetry = telemetry
        self._middleware = middleware or [correlation_middleware, timing_middleware]
        self._stream = sys.stdout if config.sink == OutputSink.STDOUT else sys.stderr

    async def execute(self) -> None:
        ctx = GreetingContext(
            correlation_id=str(uuid.uuid4()),
            locale=self._config.locale,
            plugin_name=self._pick_plugin_name(),
        )

        async def terminal(ctx: GreetingContext) -> None:
            await self._produce_and_emit(ctx)

        handler: Callable[[GreetingContext], Awaitable[None]] = terminal
        for mw in reversed(self._middleware):
            handler = self._wrap(mw, handler)

        await handler(ctx)

    def _pick_plugin_name(self) -> str:
        if self._flags.is_enabled("shouting_greeter_enabled"):
            return "shouting"
        return self._config.plugin

    @staticmethod
    def _wrap(
        mw: Middleware, nxt: Callable[[GreetingContext], Awaitable[None]]
    ) -> Callable[[GreetingContext], Awaitable[None]]:
        async def wrapped(ctx: GreetingContext) -> None:
            await mw(ctx, nxt)
        return wrapped

    async def _produce_and_emit(self, ctx: GreetingContext) -> None:
        started: GreetingStartedPayload = {
            "correlation_id": ctx.correlation_id,
            "locale": ctx.locale,
            "plugin": ctx.plugin_name,
        }
        self._telemetry.report("greeting.started", started)

        plugin = self._plugins.get(ctx.plugin_name)
        ctx.message = plugin.produce(ctx.locale)

        self._stream.write(ctx.message + self._config.terminator)
        self._stream.flush()
        ctx.characters_emitted = len(ctx.message)

        duration = time.perf_counter() - ctx.started_at
        self._metrics.greetings_total.inc(locale=ctx.locale, plugin=ctx.plugin_name)
        self._metrics.characters_emitted_total.inc(ctx.characters_emitted)
        self._metrics.greeting_duration_seconds.observe(duration)

        completed: GreetingCompletedPayload = {
            "correlation_id": ctx.correlation_id,
            "characters_emitted": ctx.characters_emitted,
            "duration_seconds": duration,
        }
        self._telemetry.report("greeting.completed", completed)


# ---------------------------------------------------------------------------
# Health endpoint
# ---------------------------------------------------------------------------

async def serve_health(
    host: str = "0.0.0.0", port: int = 8080
) -> asyncio.Server:
    async def handler(
        reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        try:
            request_line = await reader.readline()
            await reader.readuntil(b"\r\n\r\n")
        except asyncio.IncompleteReadError:
            writer.close()
            return
        path = b"/"
        parts = request_line.split(b" ")
        if len(parts) >= 2:
            path = parts[1]
        if path in (b"/healthz", b"/readyz"):
            body = b'{"status":"ok"}'
            status = b"200 OK"
        else:
            body = b'{"error":"not found"}'
            status = b"404 Not Found"
        response = (
            b"HTTP/1.1 " + status + b"\r\n"
            b"Content-Type: application/json\r\n"
            b"Content-Length: " + str(len(body)).encode() + b"\r\n\r\n" + body
        )
        writer.write(response)
        await writer.drain()
        writer.close()

    server = await asyncio.start_server(handler, host, port)
    logger.info("Health endpoint listening on %s:%d", host, port)
    return server


# ---------------------------------------------------------------------------
# Application lifecycle
# ---------------------------------------------------------------------------

@asynccontextmanager
async def application_lifecycle(
    config: GreetingConfig, metrics: MetricsRegistry
) -> AsyncIterator[None]:
    logger.info("HelloWorld v2.0.0-rc.3 bootstrap initiated")
    servers: list[asyncio.Server] = []
    if config.enable_health:
        servers.append(await serve_health(port=config.health_port))
    if config.enable_metrics:
        servers.append(await serve_metrics(metrics, port=config.metrics_port))
    try:
        yield
    finally:
        for server in servers:
            server.close()
        for server in servers:
            await server.wait_closed()
        logger.info("HelloWorld shutdown complete")


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def build_orchestrator(
    config: GreetingConfig | None = None,
) -> tuple[GreetingOrchestrator, MetricsRegistry, GreetingConfig]:
    resolved = config or GreetingConfig.from_environment()
    plugins = PluginRegistry()
    flags = ChainedFeatureFlagProvider([EnvironmentFeatureFlagProvider()])
    metrics = MetricsRegistry()
    telemetry = LoggingTelemetryReporter()
    orchestrator = GreetingOrchestrator(
        config=resolved,
        plugins=plugins,
        flags=flags,
        metrics=metrics,
        telemetry=telemetry,
    )
    return orchestrator, metrics, resolved
