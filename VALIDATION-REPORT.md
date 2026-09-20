# SBJ Decision Record V2.0 — Internal Technical Conformance Report

**Schema:** `urn:sbj:decision-record:schema:2.0.0`  
**Validation label:** INTERNAL TECHNICAL CONFORMANCE / VALIDATION

## Result

The release was validated against the included conformance fixtures.

### Valid fixtures

- A — PASS
- B — PASS
- C — PASS
- D — PASS
- E — PASS
- F — PASS
- G — PASS
- H — PASS

### Invalid/adversarial fixtures

- 01 — missing canonical core field — FAIL as expected
- 02 — invalid enumeration — FAIL as expected
- 03 — malformed timestamp — FAIL as expected
- 04 — missing activated-profile hard requirement — FAIL as expected
- 05 — unauthorized Effective Context State field — FAIL as expected
- 06 — structurally detectable secret/credential field — FAIL as expected
- 07 — invalid evidence-reference structure — FAIL as expected
- 08 — inconsistent restart/resumption disposition — FAIL as expected
- 09 — transition missing Transition Authorization reference — FAIL as expected
- 10 — authorization change missing authorization-state-change data — FAIL as expected

**Total:** 18 / 18 expected fixture outcomes reproduced.

JSON Schema Draft 2020-12 integrity was also verified during technical release adjudication.

## What this result means

The result establishes that the included reference validator and schema behave as expected against the included internal technical conformance suite.

## What this result does not mean

It is not:

- independent external validation;
- external certification;
- V2.0 architecture benchmark validation;
- proof of completeness;
- proof of regulatory compliance;
- proof of safety, correctness, or universal applicability.

The fixtures test implementation behavior, not external validation of the architecture.
