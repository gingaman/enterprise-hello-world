# HelloWorld™

[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-14%25-red)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![K8s](https://img.shields.io/badge/kubernetes-ready-blue)]()
[![SOC2](https://img.shields.io/badge/SOC2-in_progress-yellow)]()
[![Slack](https://img.shields.io/badge/slack-%23platform--helloworld-4A154B)]()

> **HelloWorld™** is a cloud-native, horizontally scalable, observability-first
> greeting orchestration platform. Built on modern Python, deployed on
> Kubernetes, instrumented with Prometheus, governed by a rigorous Contributor
> License Agreement, and aligned with the organisation's 2026 Digital Salutation
> Strategy.

## Mission

To democratise salutations at planetary scale.

## Vision

A world in which every process, thread, container, and lambda can greet every
other process, thread, container, and lambda — securely, observably, and with
zero trust.

## Principles

1. **Everything is a plugin.** Hard-coding is technical debt.
2. **Observability is not optional.** If it isn't measured, it didn't happen.
3. **Configuration over code.** Except when code over configuration.
4. **Fail fast, recover faster.** Ideally before anyone notices.
5. **No strings attached** (except the one we print).

## Architecture

```
   ┌─────────────────────────────────────────────────────────┐
   │                HelloWorld Control Plane                 │
   │                                                         │
   │  ┌───────────┐   ┌──────────┐   ┌─────────────┐         │
   │  │  Feature  │   │  Plugin  │   │  Telemetry  │         │
   │  │   Flags   │   │ Registry │   │   Pipeline  │         │
   │  └─────┬─────┘   └────┬─────┘   └──────┬──────┘         │
   │        │              │                │                │
   │        └──────┬───────┴────────┬───────┘                │
   │               │                │                        │
   │        ┌──────▼────────────────▼──────┐                 │
   │        │   Greeting Orchestrator      │                 │
   │        │   (middleware chain)         │                 │
   │        └──────────────┬───────────────┘                 │
   │                       │                                 │
   │                ┌──────▼──────┐                          │
   │                │   Emitter   │                          │
   │                └──────┬──────┘                          │
   └───────────────────────┼─────────────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │   stdout    │
                    └─────────────┘

   Observability sidecars:
     :8080/healthz       │ liveness
     :8080/readyz        │ readiness
     :9090/metrics       │ Prometheus scrape
```

## Quick Start

```bash
# Local development
python -m helloworld

# With full observability stack
HELLOWORLD_ENABLE_HEALTH=true \
HELLOWORLD_ENABLE_METRICS=true \
  python -m helloworld

# Production
kubectl apply -f k8s/
```

## Supported Locales

| Locale | Status       | Message          |
|--------|--------------|------------------|
| en-GB  | GA           | `Hello, World!`  |
| en-US  | GA           | `Hello, World!`  |
| fr-FR  | Roadmap      | Q3 2026          |
| de-DE  | Roadmap      | Q4 2026          |

## Service Level Objectives

- **Availability:** 99.95% (rolling 30-day)
- **P99 greeting latency:** < 50ms
- **Mean time to greet:** < 10ms
- **Error budget burn rate alert:** 2× for 1h, 14× for 6h

## Enterprise Greeting Governance

The **Greeting Change Advisory Board (GCAB)** supervises all changes to
punctuation, including the removal, insertion or strategic repositioning of
the exclamation mark. A **90-calendar-day rollback window** applies to
approved punctuation changes.

- [GCAB charter and change-control policy](./docs/governance/GREETING_CHANGE_ADVISORY_BOARD.md)
- [SEV-1: Global Salutation Degradation (fictional incident)](./docs/incidents/SEV-001-global-salutation-degradation.md)
- [ADR-0042: Punctuation Assurance Middleware (proposed, not implemented)](./docs/adr/ADR-0042-punctuation-assurance-middleware.md)

The illustrative incident affected 0.003% of greetings, none of which
actually happened. Its most important outcome was the recommendation
to add middleware rather than fix a string.

## Enterprise Salutation Transformation 2.1

The strategic response to a single line of terminal output now includes seven
fictional workstreams, a self-healing reinterpretation of Kubernetes restarts,
and an executive dashboard which measures organisational confidence rather
than operational evidence. **These are satirical proposals, not implemented
features or claims about real system behaviour.**

- [2.1 transformation portfolio and seven linked initiatives](./docs/strategy/HELLOWORLD_2_1_TRANSFORMATION.md)
- [Self-Healing Salutation Framework (fictional proposal)](./docs/operations/SELF_HEALING_SALUTATION.md)
- [SEV-2: Autonomous Recovery Saturation (fictional incident)](./docs/incidents/SEV-002-autonomous-recovery-saturation.md)
- [Executive dashboard: mock data and notes](./docs/dashboard/EXECUTIVE_DASHBOARD.md) ([standalone static HTML](./docs/dashboard/index.html))
- [Fictional board minutes: the 24-month transformation decision](./docs/board/BOARD-MINUTES-2026-11-09.md)

## Compliance

HelloWorld™ processes no personal data and contains no plumbing. Both facts
have been formally assessed.

- [Data Protection Notice and DPIA](./docs/compliance/DATA_PROTECTION.md) — UK GDPR, lawful basis, and the right to erase the World
- [Facilities and Welfare Compliance Statement](./docs/compliance/FACILITIES_AND_WELFARE.md) — sanitary provision, and who owns the toilet policy (nobody)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). All contributors must sign the CLA
before submitting changes, including whitespace and semicolon adjustments.

## Licence

MIT. Legal were consulted in Q2 and have yet to reply. The project is
proceeding under the assumption that silence constitutes approval.

---

_HelloWorld™ is a trademark of HelloWorld Platform Team. All rights reserved._
