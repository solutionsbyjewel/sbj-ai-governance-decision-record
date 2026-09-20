# Conditional Validation and Profile Activation

Profiles A–G are conditional views of one Decision Record, not separate record types and not new architecture.

## Profiles

- A — Authorization Change
- B — Delegation / Multi-Agent Execution
- C — Consequential Execution
- D — Physical AI
- E — Transition
- F — Incident / Recovery / Restart
- G — Shared-Responsibility Deployment

## Why profile activation is external

Several profile activations depend on governance **materiality**. JSON Schema can validate syntax, structure, and deterministic relationships, but raw field presence cannot prove that a condition is materially significant to the governance determination.

The reference validator therefore accepts activated profile IDs as external context:

```bash
python validator/validate.py fixtures/valid/D.json --profiles B,C
```

The profile IDs supplied to the validator are not stored in the canonical Decision Record object.

## Deterministic rules

Rules that follow directly from frozen semantics are encoded in the schema, including examples such as:

- `TRANSITION` requires a Transition Authorization reference;
- material authorization-state-changing event types require authorization-state-change data;
- `RESTART` / `RESUMPTION` require the corresponding restart/resumption determination;
- explicit `*_WITH_CONDITIONS` dispositions require a reassessment condition.

See `rules/deterministic-cross-field-rules.json` for the machine-readable inventory.
