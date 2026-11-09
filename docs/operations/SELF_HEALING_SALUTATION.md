# Self-Healing Salutation Framework™ (SHSF)

**Status:** Proposed narrative overlay; **not implemented**  
**Type:** Satirical operations framework  
**Design principle:** A restart is a recovery, except when somebody calls it a failure.

## The inconvenient technical detail

The existing Python entry point emits one greeting and then exits with a successful
status. The Kubernetes Deployment requests three long-running replicas.
Under the Deployment's normal restart policy, the container will be restarted
after completion. Restarting repeatedly is **not a sign of service health** and
may create back-off delays and unavailable ready replicas.

The project must not misrepresent this as working self-healing software.

## Proposed management reinterpretation

For a fictional scenario, classify each repeated container start as an
**Autonomous Salutation Recovery Event (ASRE)**. This preserves the external
story that the platform is resilient while conceding in the footnotes that
nothing malfunctioned in the Python process itself.

### Glossary

| Technical observation | Proposed management label |
|---|---|
| Container exits after successful print | Graceful greeting-cycle completion |
| Deployment restarts the container | Autonomous service restoration |
| Pods do not remain ready | Elastic readiness optimisation |
| Restart count rises | Resilience throughput |
| CrashLoopBackOff / restart back-off | Controlled greeting-rate protection |

## Proposed event-handling flow

```text
Python process prints "Hello, World!"
                 |
             exits 0
                 |
Kubernetes Deployment restarts the container
                 |
         restart count rises
                 |
Management dashboard counts an "autonomous recovery"
                 |
SRE files a note explaining why this is not success
                 |
             note deferred
```

## Guardrails for the mock dashboard

1. All illustrative recovery totals must be conspicuously labelled as fictional.
2. Never present restart counts as proof of a healthy Deployment.
3. Do not invent an operational Prometheus metric or live connection.
4. A possible real fix would be a Kubernetes Job or a process that genuinely stays running, but this programme deliberately declines to implement it.
5. No real alerting, readiness probe or success criterion is modified.

## Board proposition

Do not solve the problem before the Resilience Narrative Harmonisation
Workstream has established the language in which the solution will be reported.

See [SEV-2 simulated incident](../incidents/SEV-002-autonomous-recovery-saturation.md) and [executive dashboard](../dashboard/EXECUTIVE_DASHBOARD.md).

