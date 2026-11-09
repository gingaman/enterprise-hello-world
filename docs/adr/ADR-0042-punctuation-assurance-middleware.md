# ADR-0042: Introduce Punctuation Assurance Middleware

**Status:** Proposed; awaiting GCAB approval  
**Decision owners:** Platform Architecture, Enterprise Salutation Governance  
**Context:** [INC-SAL-0001](../incidents/SEV-001-global-salutation-degradation.md) (fictional incident)

> This ADR is satire. The middleware described here is deliberately **not implemented**.

## Context

HelloWorld™ already has correlation and timing middleware. A simulated
SEV-1 incident demonstrated a previously unrecognised enterprise risk:
a greeting might remain available, observable and scalable while losing
its exclamation mark.

The immediate engineering remedy would be to validate the emitted string.
That approach was considered too direct and insufficiently platform-oriented.

## Decision proposed

Add a dedicated **Punctuation Assurance Middleware (PAM)** stage to the
Greeting Orchestrator. PAM will:

1. Obtain an approved punctuation policy from the future Punctuation Policy Service
2. Compare the proposed greeting against its signed punctuation baseline
3. Raise a non-compliance event for unexpected enthusiasm loss
4. Record a Punctuation Integrity Attestation before permitting emission
5. Route disputed characters to the GCAB for non-blocking deliberation, subject to a blocking policy decision

Illustrative target architecture:

```text
Feature Flags ─┐
Plugin Registry ├─> Greeting Orchestrator
Telemetry ─────┘          |
                   Correlation Middleware
                          |
                     Timing Middleware
                          |
               Punctuation Assurance Middleware
                          |
                        Emitter
                          |
                        stdout
```

## Consequences

- Another middleware stage is added to the execution path of a constant string.
- An independently deployable policy service becomes a potential dependency.
- A new operational dashboard can display punctuation integrity.
- The platform will become more defensible at architecture reviews.
- The one-line alternative remains available for consideration in a subsequent financial year.

## Alternatives rejected

| Alternative | Reason for rejection |
|---|---|
| `print("Hello, World!")` | No evidence of enterprise readiness |
| `assert message.endswith("!")` | Insufficient governance surface area |
| Additional unit test | Does not create a new platform workstream |
| Do nothing | Already the implicit operating model |

## Rollout constraints

No implementation work may begin until a GPCR and the required approvals have
been recorded under the [GCAB policy](../governance/GREETING_CHANGE_ADVISORY_BOARD.md).
Any production punctuation change must preserve a tested rollback route for
90 calendar days.

This proposal does not modify running behaviour, monitoring or Kubernetes deployment.
