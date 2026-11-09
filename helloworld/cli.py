"""
helloworld.cli
==============

Command-line entry point for HelloWorld™.
"""

from __future__ import annotations

import asyncio
import logging
import os
import sys

from .core import application_lifecycle, build_orchestrator


def _configure_logging() -> None:
    logging.basicConfig(
        level=os.environ.get("HELLOWORLD_LOG_LEVEL", "INFO"),
        format="%(asctime)s | %(levelname)-8s | %(name)-28s | %(message)s",
    )


async def _run() -> int:
    _configure_logging()
    orchestrator, metrics, config = build_orchestrator()
    async with application_lifecycle(config, metrics):
        try:
            await orchestrator.execute()
            return 0
        except Exception as exc:
            logging.getLogger("helloworld.cli").error(
                "Greeting pipeline failed: %s", exc, exc_info=True
            )
            return 1


def main() -> None:
    sys.exit(asyncio.run(_run()))


if __name__ == "__main__":
    main()
