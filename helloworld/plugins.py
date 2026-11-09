"""
helloworld.plugins
==================

Plugin registry and built-in greeter implementations.

External plugins may be registered via the `helloworld.plugins` entry point
group in the contributing package's `pyproject.toml`.
"""

from __future__ import annotations

import logging
from typing import Protocol, runtime_checkable

logger = logging.getLogger("helloworld.plugins")


# ---------------------------------------------------------------------------
# Plugin protocol
# ---------------------------------------------------------------------------

@runtime_checkable
class GreeterPlugin(Protocol):
    """Structural interface that all greeter plugins must satisfy."""

    name: str

    def produce(self, locale: str) -> str: ...


# ---------------------------------------------------------------------------
# Built-in plugins
# ---------------------------------------------------------------------------

class DefaultGreeter:
    name = "default"

    _catalogue = {
        "en-GB": "Hello, World!",
        "en-US": "Hello, World!",
    }

    def produce(self, locale: str) -> str:
        return self._catalogue.get(locale, self._catalogue["en-GB"])


class ShoutingGreeter:
    """Produces an upper-cased greeting with configurable exclamation count."""

    name = "shouting"

    def __init__(self, exclamations: int = 3) -> None:
        self._exclamations = exclamations

    def produce(self, locale: str) -> str:
        base = DefaultGreeter().produce(locale).rstrip("!")
        return base.upper() + ("!" * self._exclamations)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

class PluginRegistry:
    """In-memory plugin registry.

    Discovers built-in plugins on construction. External plugins registered
    via entry points will be added in v2.1 (see ADR-0037).
    """

    def __init__(self) -> None:
        self._plugins: dict[str, GreeterPlugin] = {}
        self._register_builtins()

    def _register_builtins(self) -> None:
        for plugin in (DefaultGreeter(), ShoutingGreeter()):
            self.register(plugin)

    def register(self, plugin: GreeterPlugin) -> None:
        if plugin.name in self._plugins:
            logger.warning("Plugin %r already registered; overwriting", plugin.name)
        self._plugins[plugin.name] = plugin
        logger.debug("Registered plugin: %s", plugin.name)

    def get(self, name: str) -> GreeterPlugin:
        if name not in self._plugins:
            raise KeyError(f"No plugin registered with name: {name!r}")
        return self._plugins[name]

    def names(self) -> list[str]:
        return sorted(self._plugins.keys())
