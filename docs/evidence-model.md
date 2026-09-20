# Reference-First Evidence Model

The SBJ Decision Record references authoritative evidence rather than duplicating the evidence repository.

The canonical core separates two questions:

1. **What evidence supported the governance determination?** → `record.evidence_refs`
2. **Was that evidence sufficient for this governance determination?** → `record.evidence_sufficiency`

An evidence reference can identify its evidence type while keeping the authoritative content in the source system. This avoids turning the Decision Record into an evidence warehouse.

Evidence existence does not prove sufficiency. The controlled sufficiency values support `SUFFICIENT`, `SUFFICIENT_WITH_LIMITATIONS`, `INSUFFICIENT`, `CONFLICTING`, `INCOMPLETE`, `STALE`, and constrained `NOT_APPLICABLE`.

Material adverse evidence must remain representable and should not be hidden by favorable evidence.

The Decision Record does not require chain-of-thought, hidden internal state, or exhaustive transformation history.
