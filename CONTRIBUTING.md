# Contributing to HelloWorld™

Thank you for your interest in contributing to HelloWorld™. We take pride in
the quality of our codebase, and we maintain that quality through a rigorous
and thoroughly documented contribution process.

## Before You Begin

All contributors must:

1. Sign the [Contributor License Agreement](./CLA.md). This applies to all
   contributions, including but not limited to:
   - Code changes (including single-character fixes)
   - Documentation updates (including typo corrections)
   - Semicolon additions or removals
   - Whitespace modifications (tabs vs. spaces handled under separate policy)
   - Comment updates
   - File renames

2. Complete the **HelloWorld™ Certified Contributor** training programme
   (16 hours, available in e-learning portal). Certification valid for
   12 months; renewal required annually.

3. Attend the monthly **Architecture Review Board (ARB)** meeting to present
   your proposed change. Slide deck template available on the internal wiki
   (30-slide minimum, 50-slide maximum). Remote attendance permitted for
   contributors in GMT ± 3.

4. Obtain written sign-off from:
   - Three (3) Principal Engineers
   - One (1) Staff Engineer (domain-aligned)
   - One (1) Engineering Director
   - One (1) Security representative (for any change touching a string literal)

## Pull Request Checklist

- [ ] CLA signed and notarised
- [ ] ARB presentation slides attached (as `.pptx`, not `.key`)
- [ ] Architecture Decision Record (ADR) filed in `docs/adr/`
- [ ] Threat model updated (STRIDE methodology)
- [ ] SOC2 compliance impact assessment complete
- [ ] Data Protection Impact Assessment (DPIA) complete, if the greeting
      contains or could in future contain personally identifiable information
- [ ] Unit test coverage ≥ 80% (current repository sits at 14%; this
      threshold does not apply retroactively)
- [ ] Integration tests pass in staging
- [ ] Performance regression benchmarks executed on bare metal (AWS
      c7i.metal-24xl recommended)
- [ ] Chaos engineering review complete (inject one (1) pod eviction)
- [ ] Accessibility review complete (WCAG 2.2 AAA)
- [ ] Internationalisation review complete (all two (2) supported locales)
- [ ] README badges updated
- [ ] CHANGELOG entry in correct format (see `docs/CHANGELOG_FORMAT.md`)
- [ ] Jira ticket linked, labelled, and scheduled to a sprint
- [ ] Confluence page updated
- [ ] Slack thread opened in `#platform-helloworld` and left open for at
      least five (5) business days for asynchronous review

## Response Times

We aim to respond to pull requests within four (4) business quarters.

For urgent changes (defined as: production outage actively losing revenue),
please use the `break-glass` label. Break-glass PRs bypass CLA verification
but still require ARB review; the ARB meets within 72 hours of a break-glass
request being filed.

## Commit Message Format

```
<type>(<scope>)!: <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`,
`ci`, `chore`, `revert`, `ceremony`.

Scopes: `core`, `plugins`, `metrics`, `health`, `feature-flags`, `observability`,
`governance`, `platform`, `meta`.

Breaking changes must be indicated with `!` and described in the footer with
`BREAKING CHANGE:` followed by a migration guide and a 90-day deprecation plan.

## Code of Conduct

See `CODE_OF_CONDUCT.md`. TL;DR: be excellent to each other. Slightly less
excellent to the CI pipeline is permitted.

## Questions

If you have questions, please do not email the maintainers directly. Instead,
open a GitHub Discussion, tag it `question`, wait for triage (SLA: 10
business days), then follow up in Slack.

Thank you for contributing to HelloWorld™.
