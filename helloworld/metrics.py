"""
helloworld.metrics
==================

Prometheus-compatible metrics registry and exposition.

Metrics are exposed via an HTTP endpoint at `/metrics` on the configured
metrics port (default 9090) when `HELLOWORLD_ENABLE_METRICS=true`.
"""

from __future__ import annotations

import asyncio
import logging
import time
from collections import defaultdict
from typing import Mapping

logger = logging.getLogger("helloworld.metrics")


# ---------------------------------------------------------------------------
# Metric types
# ---------------------------------------------------------------------------

class Counter:
    def __init__(self, name: str, help_text: str, labels: tuple[str, ...] = ()) -> None:
        self.name = name
        self.help = help_text
        self.label_names = labels
        self._values: dict[tuple[str, ...], float] = defaultdict(float)

    def inc(self, amount: float = 1.0, **label_values: str) -> None:
        key = tuple(label_values.get(name, "") for name in self.label_names)
        self._values[key] += amount

    def expose(self) -> str:
        lines = [f"# HELP {self.name} {self.help}", f"# TYPE {self.name} counter"]
        for key, value in self._values.items():
            label_str = self._format_labels(key)
            lines.append(f"{self.name}{label_str} {value}")
        return "\n".join(lines)

    def _format_labels(self, key: tuple[str, ...]) -> str:
        if not self.label_names:
            return ""
        pairs = ",".join(
            f'{name}="{value}"' for name, value in zip(self.label_names, key)
        )
        return "{" + pairs + "}"


class Histogram:
    _BUCKETS = (0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0, float("inf"))

    def __init__(self, name: str, help_text: str) -> None:
        self.name = name
        self.help = help_text
        self._counts = [0] * len(self._BUCKETS)
        self._sum = 0.0
        self._count = 0

    def observe(self, value: float) -> None:
        self._sum += value
        self._count += 1
        for i, bound in enumerate(self._BUCKETS):
            if value <= bound:
                self._counts[i] += 1

    def expose(self) -> str:
        lines = [f"# HELP {self.name} {self.help}", f"# TYPE {self.name} histogram"]
        for bound, count in zip(self._BUCKETS, self._counts):
            bound_str = "+Inf" if bound == float("inf") else str(bound)
            lines.append(f'{self.name}_bucket{{le="{bound_str}"}} {count}')
        lines.append(f"{self.name}_sum {self._sum}")
        lines.append(f"{self.name}_count {self._count}")
        return "\n".join(lines)


class Gauge:
    def __init__(self, name: str, help_text: str) -> None:
        self.name = name
        self.help = help_text
        self._value = 0.0

    def set(self, value: float) -> None:
        self._value = value

    def expose(self) -> str:
        return (
            f"# HELP {self.name} {self.help}\n"
            f"# TYPE {self.name} gauge\n"
            f"{self.name} {self._value}"
        )


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

class MetricsRegistry:
    def __init__(self) -> None:
        self.greetings_total = Counter(
            "helloworld_greetings_total",
            "Total number of greetings emitted",
            ("locale", "plugin"),
        )
        self.characters_emitted_total = Counter(
            "helloworld_characters_emitted_total",
            "Total number of characters emitted across all greetings",
        )
        self.greeting_duration_seconds = Histogram(
            "helloworld_greeting_duration_seconds",
            "Time spent producing and emitting a greeting",
        )
        self.build_info = Gauge(
            "helloworld_build_info",
            "HelloWorld build metadata (value is always 1)",
        )
        self.build_info.set(1)
        self._started_at = time.time()

    def expose(self) -> str:
        return "\n\n".join(
            [
                self.greetings_total.expose(),
                self.characters_emitted_total.expose(),
                self.greeting_duration_seconds.expose(),
                self.build_info.expose(),
                f"helloworld_uptime_seconds {time.time() - self._started_at}",
            ]
        )


# ---------------------------------------------------------------------------
# Exposition server
# ---------------------------------------------------------------------------

async def serve_metrics(
    registry: MetricsRegistry, host: str = "0.0.0.0", port: int = 9090
) -> asyncio.Server:
    async def handler(
        reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        try:
            await reader.readuntil(b"\r\n\r\n")
        except asyncio.IncompleteReadError:
            writer.close()
            return
        body = registry.expose().encode()
        response = (
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain; version=0.0.4\r\n"
            b"Content-Length: " + str(len(body)).encode() + b"\r\n\r\n" + body
        )
        writer.write(response)
        await writer.drain()
        writer.close()

    server = await asyncio.start_server(handler, host, port)
    logger.info("Metrics endpoint listening on %s:%d/metrics", host, port)
    return server
