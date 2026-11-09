# Greeting Change Advisory Board (GCAB)

**Policy ID:** GCAB-001  
**Status:** Mandatory, subject to ratification  
**Owner:** Enterprise Salutation Governance Office  
**Scope:** All environments, including developer laptops that might become production-adjacent

> This is fictional enterprise-IT satire, not an operational change-control policy.

## Charter

The GCAB exists to safeguard the strategic punctuation posture of HelloWorld™.
Its guiding principle is that no punctuation change is too small to require executive oversight.

**Approval is required before any change to greeting punctuation**, including
an exclamation mark, comma, full stop, apostrophe, quotation mark, or line
terminator. Changes that *do not* alter punctuation must be reviewed to
demonstrate that they do not alter punctuation.

## Membership and quorum

A quorate meeting requires:

- A chair from Enterprise Salutation Governance
- Three Principal Engineers, none of whom may have authored the change
- A Security representative with string-literal clearance
- A Site Reliability Engineer to explain why the change is unnecessary
- A Legal observer, whose silence must not be construed as approval unless useful

The original author may attend to answer questions but may not vote.
The chair has a casting vote only when the proposed punctuation is fashionable.

## Mandatory change dossier

Every Greeting Punctuation Change Request (GPCR) must contain:

1. The existing greeting, the proposed greeting and a character-by-character diff
2. A business case with a quantified return on exclamation
3. A STRIDE threat model covering punctuation loss, injection and unauthorised enthusiasm
4. Accessibility and internationalisation impact assessments for both supported English locales
5. A full disaster-recovery rehearsal and evidence of three independent approvals
6. A rollback plan capable of restoring the previous punctuation byte for byte

A single-character change remains a breaking change until the GCAB determines otherwise.

## The 90-day rollback window

For **90 calendar days after first production emission**, the previous approved
punctuation must remain recoverable through a tested, documented rollback mechanism.
The new punctuation must be monitored throughout this window.

Rollback itself requires a fresh GPCR, except during an active SEV-1, when an
emergency GCAB may be convened within 72 hours. An emergency rollback does not
waive the post-rollback presentation, currently expected to take 30–50 slides.

The 90-day rollback window is separate from, and may overlap with, the existing
90-day breaking-change deprecation plan.

## Service levels

- Standard GPCR response target: four business quarters
- Urgent GPCR response target: the next quarterly scheduling review
- Emergency SEV-1 meeting target: 72 hours
- Success measure: percentage of punctuation changes prevented, including beneficial ones

## Related material

- [Contributing guide](../../CONTRIBUTING.md)
- [SEV-1: Global Salutation Degradation](../incidents/SEV-001-global-salutation-degradation.md)
- [ADR-0042: Punctuation Assurance Middleware](../adr/ADR-0042-punctuation-assurance-middleware.md)

*The GCAB reserves the right to issue a correction to this policy once the correction has been approved by the GCAB.*
