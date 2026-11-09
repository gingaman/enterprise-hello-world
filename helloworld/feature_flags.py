"""
helloworld.feature_flags
========================

Feature flag provider abstraction with multiple backend implementations.

The `RemoteFeatureFlagProvider` is currently a stub; remote flag evaluation
will be enabled in v2.1 once the distributed flag mesh is generally available
(see ADR-0041).
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Protocol, runtime_checkable

logger = logging.getLogger("helloworld.feature_flags")


# ---------------------------------------------------------------------------
# Known flags
# ---------------------------------------------------------------------------

KNOWN_FLAGS: dict[str, bool] = {
    "shouting_greeter_enabled": False,
    "greeting_cache_enabled": False,
    "per_character_delay_enabled": False,
    "structured_logging_enabled": True,
    "legacy_plain_output": True,
}


# ---------------------------------------------------------------------------
# Provider protocol
# ---------------------------------------------------------------------------

@runtime_checkable
class FeatureFlagProvider(Protocol):
    def is_enabled(self, flag: str) -> bool: ...


# ---------------------------------------------------------------------------
# Implementations
# ---------------------------------------------------------------------------

class EnvironmentFeatureFlagProvider:
    """Reads flags from environment variables: `HELLOWORLD_FF_<FLAG_NAME>`."""

    _ENV_PREFIX = "HELLOWORLD_FF_"

    def is_enabled(self, flag: str) -> bool:
        if flag not in KNOWN_FLAGS:
            logger.warning("Unknown feature flag queried: %s", flag)
        env_key = self._ENV_PREFIX + flag.upper()
        raw = os.environ.get(env_key)
        if raw is None:
            return KNOWN_FLAGS.get(flag, False)
        return raw.strip().lower() in {"1", "true", "yes", "on"}


class FileFeatureFlagProvider:
    """Reads flags from a JSON file, falling back to defaults."""

    def __init__(self, path: Path) -> None:
        self._path = path
        self._cache: dict[str, bool] | None = None

    def _load(self) -> dict[str, bool]:
        if self._cache is not None:
            return self._cache
        try:
            with self._path.open() as f:
                data = json.load(f)
            self._cache = {k: bool(v) for k, v in data.items()}
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("Failed to load feature flags from %s: %s", self._path, exc)
            self._cache = {}
        return self._cache

    def is_enabled(self, flag: str) -> bool:
        return self._load().get(flag, KNOWN_FLAGS.get(flag, False))


class RemoteFeatureFlagProvider:
    """Stub for remote flag evaluation. Returns defaults until v2.1."""

    def __init__(self, endpoint: str) -> None:
        self._endpoint = endpoint
        logger.info(
            "RemoteFeatureFlagProvider initialised (endpoint=%s); "
            "remote evaluation pending v2.1",
            endpoint,
        )

    def is_enabled(self, flag: str) -> bool:
        return KNOWN_FLAGS.get(flag, False)


# ---------------------------------------------------------------------------
# Chained provider
# ---------------------------------------------------------------------------

class ChainedFeatureFlagProvider:
    """Evaluates flags through an ordered chain of providers.

    First provider to return a non-default value wins. Simpler than it sounds;
    more complicated than it needs to be.
    """

    def __init__(self, providers: list[FeatureFlagProvider]) -> None:
        self._providers = providers

    def is_enabled(self, flag: str) -> bool:
        for provider in self._providers:
            try:
                return provider.is_enabled(flag)
            except Exception as exc:
                logger.warning(
                    "Provider %s raised while evaluating %s: %s",
                    type(provider).__name__, flag, exc,
                )
                continue
        return KNOWN_FLAGS.get(flag, False)
