# SEV-1: Global Salutation Degradation

**Incident ID:** INC-SAL-0001  
**Severity:** SEV-1 / Existential punctuation event  
**Status:** Post-incident review complete; technical remediation awaiting governance  
**Nature:** **Fictional incident, created for satire. No actual outage or measurements are claimed.**

## Executive summary

In this simulated production incident, **0.003% of greetings** were delivered
without the mandatory exclamation mark:

```diff
- Hello, World!
+ Hello, World
```

No greetings were lost. No user data were compromised. The organisation
nevertheless experienced a catastrophic deterioration in perceived
salutational confidence. The Executive Salutation Sponsor requested an
immediate briefing and a fresh dashboard.

## Customer impact

- Affected greetings: **0.003%** (illustrative scenario, not observed telemetry)
- Availability: unaffected
- Punctuation integrity: **99.997%**
- Reputational impact: provisionally classified as immeasurable
- Revenue at risk: pending Finance confirmation that greetings generate revenue

## Simulated timeline

| Relative time | Event |
|---|---|
| T+00:00 | A greeting is emitted without its closing exclamation mark |
| T+00:02 | Monitoring reports normal uptime and a healthy character-emission counter |
| T+00:17 | A stakeholder notices that a greeting appears insufficiently enthusiastic |
| T+00:25 | Incident declared SEV-1; virtual war room established |
| T+01:10 | Seven workstreams formed to identify an owner for the missing character |
| T+04:00 | Punctuation restored through an undocumented manual change |
| T+72:00 | Emergency change board convenes to decide whether the restoration was authorised |
| T+90 days | Earliest proposed end of the mandatory rollback-observation window |

## Findings

**Immediate failure mode:** the greeting-emission path had no dedicated
punctuation-integrity enforcement stage. Existing metrics counted characters
but did not assess whether the final character met corporate policy.

**Root cause, as agreed by management:** insufficient cross-functional
governance. Engineering proposed a one-line assertion; the review rejected it
as insufficiently strategic.

**Contributing factors:**

1. The test suite checks one expected greeting and does not independently certify exclamation-mark continuity.
2. Existing architecture has middleware for correlation and timing, but none specifically responsible for enthusiasm.
3. There was no Greeting Change Advisory Board to decide which punctuation incidents ought to exist.
4. The organisation had not assigned a directly responsible individual to every character position.

## Corrective and preventive actions

| Action | Owner | Target | Status |
|---|---|---|---|
| Establish the GCAB | Governance | Before next punctuation change | Policy drafted |
| Propose Punctuation Assurance Middleware | Platform Engineering | After ADR review | Proposed |
| Add `helloworld_punctuation_integrity_ratio` metric | Observability | Next telemetry programme | Backlog |
| Create a per-character accountability matrix | Transformation Office | Q4, year to be agreed | Discovery |
| Add a check for `!` at the end of the greeting | Engineering | Deferred pending architectural alignment | Blocked |

The post-incident review recommends **an additional middleware layer**
instead of simply checking the string. See
[ADR-0042](../adr/ADR-0042-punctuation-assurance-middleware.md).

## Lessons learnt

- An operationally healthy platform can still fail to meet the organisation's strategic punctuation expectations.
- Every missing character is a governance opportunity.
- The corrective-action process must itself undergo a post-corrective-action review.

**Final assessment:** The incident was preventable. The review has increased
organisational confidence without yet changing the software.
