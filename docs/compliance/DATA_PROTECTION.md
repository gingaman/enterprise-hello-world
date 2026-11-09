# Data Protection Notice and DPIA

**Policy ID:** DP-001
**Status:** Live, pending sign-off by the Data Protection Officer (role vacant)
**Owner:** Enterprise Salutation Governance Office, on behalf of the Controller
**Applies to:** Every emission of `Hello, World!`, in every environment, including the ones nobody admits to

> This is satire. It is not legal advice, and HelloWorld™ processes no personal data.
> That fact has not stopped this document from being written.

## 1. Summary for data subjects

HelloWorld™ greets the World. The World contains roughly eight billion natural
persons. Legal could not rule out that at least one of them might feel
personally addressed. A Data Protection Impact Assessment (UK GDPR, Article 35)
was therefore commissioned as a precaution, and has since become a dependency.

## 2. Identity of the Controller

The Controller is HelloWorld Platform Team. The Processor is `stdout`. No
Data Processing Agreement exists with `stdout`. Procurement has been asked to
raise a purchase order with the terminal.

## 3. Categories of data processed

| Data | Category | Notes |
|---|---|---|
| `Hello` | Salutation | Not personal data. Logged anyway. |
| `,` | Punctuation | Governed by [GCAB-001](../governance/GREETING_CHANGE_ADVISORY_BOARD.md). |
| `World` | Data subject (collective) | Approximately 8.2 billion individuals. None consulted. |
| `!` | Enthusiasm | Possibly special-category data. Under review. |
| Correlation ID | Pseudonymous identifier | A random UUID that identifies one greeting, permanently, in the logs. |

## 4. Lawful basis

The lawful basis is **legitimate interests** (Article 6(1)(f)). A Legitimate
Interests Assessment found that:

- the Controller has a legitimate interest in saying hello;
- the processing is necessary, as no less intrusive greeting was identified;
- the World's interests do not override it, because the World was not asked.

**Consent** was considered and rejected. A consent banner before every greeting
was prototyped. Usability testing found that 100% of participants clicked
"Accept all" to make it go away, which the review board judged too honest.

## 5. Data subject rights

| Right | How to exercise it | Outcome |
|---|---|---|
| Access (Art. 15) | Run the program | You will receive a copy of your greeting within one month, or within 0.1 ms |
| Rectification (Art. 16) | Submit a GPCR to the GCAB | See GCAB-001; allow 90 days for rollback |
| Erasure (Art. 17) | Email the DPO (vacant) | The greeting becomes `Hello, !` |
| Restriction (Art. 18) | Set `HELLOWORLD_SINK=stderr` | You are still greeted, but less visibly |
| Objection (Art. 21) | Do not run `python -m helloworld` | Fully effective. Our best-performing control. |
| Portability (Art. 20) | Copy the string | Supplied in a structured, commonly used, machine-readable format: a string |

Requests to erase the World as a whole are out of scope and should be routed to
a different kind of platform.

## 6. Retention

Greetings are retained in `stdout` until the terminal scrolls, the window
closes, or the user types `clear`. The retention schedule is therefore set by
whoever is at the keyboard. This has been accepted as a residual risk.

Telemetry logs containing correlation IDs are retained indefinitely, because
nobody wrote a deletion job. A deletion job is on the backlog behind
Punctuation Assurance Middleware ([ADR-0042](../adr/ADR-0042-punctuation-assurance-middleware.md)).

## 7. International transfers

When the Kubernetes deployment scales out, the greeting may be emitted from any
region. The World is, by definition, in every jurisdiction. A transfer risk
assessment concluded that the greeting is already everywhere it is going.

## 8. Breaches

A personal data breach must be reported to the ICO within 72 hours of the
Controller becoming aware of it. The GCAB meets within 72 hours of an
emergency being declared. These two clocks have not yet been reconciled, and
the reconciliation is itself a workstream.

## 9. DPIA outcome

| Risk | Likelihood | Impact | Residual |
|---|---|---|---|
| A member of the World feels singled out | Low | Low | Accepted |
| Greeting emitted without lawful basis | Low | Low | Accepted, see §4 |
| DPO role remains vacant | Certain | Unknown | Escalated |
| This document is read in full | Very low | High | Mitigated by its length |

**Conclusion:** the processing may proceed. It has in fact been proceeding the
whole time; this assessment documents that retrospectively, which is how most
of them are written.
