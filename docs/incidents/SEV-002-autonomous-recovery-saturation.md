# SEV-2: Autonomous Recovery Saturation

**Incident:** INC-SAL-0002  
**Severity:** SEV-2 in this invented scenario  
**Status:** Fictional management review completed  
**Evidence:** None. All counts and times are invented for humour.

## Executive synopsis

The hypothetical HelloWorld™ Kubernetes Deployment has restarted its
single-shot application **14,392 times**, with a total of **one** greeting
counted by the imaginary management reporting system.

The Platform Engineering team identified a mismatch between the short-lived
program and the long-running Deployment. The communications team described
the same data as "14,392 successful self-healing events".

These figures are **not observations from GitHub, Kubernetes, CI or Prometheus**.

## Simulated timeline

| Time | Event |
|---|---|
| 09:00 | A single greeting is emitted and the process exits successfully |
| 09:01 | Kubernetes restarts the process as requested by the Deployment |
| 09:10 | The resilience dashboard reports an encouraging increase in recovery throughput |
| 10:00 | SRE raises concern about repeated restarts and unavailable readiness |
| 10:15 | SRE request recategorised as a terminology improvement |
| 11:00 | Communications publishes 'Platform autonomously recovered 14,392 times' |
| 12:00 | SEV-2 convened to investigate why Engineering is using the phrase 'restart loop' |

## Technical finding

A Deployment assumes a continuously running workload. A program which runs
once and terminates does not naturally satisfy that contract. This is a real
architectural observation about the checked-in source and manifest; the
14,392-event scenario is fictional.

## Satirical management root cause

**Insufficient alignment between engineering terminology and executive narrative.**

## Corrective actions

| Action | Owner | Decision |
|---|---|---|
| Consider moving batch greeting to a Job | Engineering | Deferred: insufficient architectural ambition |
| Consider keeping a legitimate service process alive | Platform | Deferred pending 24-month programme |
| Introduce Self-Healing Salutation Framework™ | Transformation | Approved in principle |
| Rename the restart-count chart 'Recovered Experiences' | Reporting | Proposed |
| Convene a retrospective on the retrospective | PMO | High priority |

## Closing statement

The service remained functionally questionable, but the programme achieved
a sustained improvement in the presentation of its operational indicators.

See [SHSF](../operations/SELF_HEALING_SALUTATION.md) and
[executive dashboard](../dashboard/EXECUTIVE_DASHBOARD.md).

