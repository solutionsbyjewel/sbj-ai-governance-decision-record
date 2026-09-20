# SBJ AI Governance Decision Record V2.0

**AI governance decision record JSON Schema, validation rules, evidence references, and conformance fixtures for attributable governance decisions.**

**Technical schema:** `urn:sbj:decision-record:schema:2.0.0`  
**Methodology:** `LOCATE → ASSIGN → RECORD → SCALE`  
**Release:** `2.0.0`  
**Status:** Technical release 2.0.0.

## What the Decision Record is

The SBJ Decision Record is a structured governance record for a **material AI governance decision or material governance event requiring an attributable determination**.

It is designed to preserve what was governed, who held accountable authority, what was decided, when the decision was made, what evidence supported it, whether that evidence was sufficient, and how broadly the determination applies.

The Decision Record can be used across human-governed AI, decision-support systems, enterprise agents, multi-agent execution, Physical AI, shared-responsibility deployments, incidents, transitions, restart/resumption decisions, and other material governance events where the approved conditional triggers apply.

## What it is not

The Decision Record is not:

- execution telemetry;
- an evidence repository;
- chain-of-thought capture;
- an incident-management platform;
- a configuration repository;
- a universal runtime trace;
- a substitute for the authoritative systems that hold evidence, provenance, telemetry, permissions, configuration, or incident data.

Those systems remain authoritative. The Decision Record references them when they are material to the governance determination.

## Methodology

The frozen Decision Record methodology is:

```text
LOCATE
  ↓
ASSIGN
  ↓
RECORD
  ↓
SCALE
```

- **LOCATE** — identify the governed subject and exact scope.
- **ASSIGN** — identify the accountable authority and material authority provenance.
- **RECORD** — preserve the governance determination, time, evidence references, evidence sufficiency, and triggered governance conditions.
- **SCALE** — determine how broadly the decision applies and when reassessment is required.

## Canonical core

Every valid Decision Record contains the nine canonical governance fields:

1. `locate.governed_subject`
2. `locate.decision_event_type`
3. `locate.governed_scope`
4. `assign.accountable_authority`
5. `record.decision_disposition`
6. `record.decision_time`
7. `record.evidence_refs`
8. `record.evidence_sufficiency`
9. `scale.scale_determination`

Administrative metadata is serialized under `record_metadata`; it does not create another methodology stage.

`record.evidence_sufficiency` is always populated. `NOT_APPLICABLE` is permitted only where evidence sufficiency genuinely does not bear on the Decision Record class. That determination remains governance/policy context; JSON Schema does not infer it.

## Evidence model: reference first

Evidence remains in its authoritative evidence system wherever practical. A Decision Record carries **references** to the evidence relied upon rather than duplicating an evidence repository.

Evidence existence does not establish evidence sufficiency. The record therefore separates:

- `record.evidence_refs` — what authoritative evidence was relied upon; from
- `record.evidence_sufficiency` — whether that evidence was sufficient for the governance determination.

Material adverse, conflicting, stale, incomplete, or insufficient evidence remains representable through the controlled values and external evidence references.

## Conditional profiles

One Decision Record supports seven approved conditional profiles:

- **A — Authorization Change**
- **B — Delegation / Multi-Agent Execution**
- **C — Consequential Execution**
- **D — Physical AI**
- **E — Transition**
- **F — Incident / Recovery / Restart**
- **G — Shared-Responsibility Deployment**

Profile membership is **not stored in the canonical Decision Record JSON object**. Profile activation remains external governance/validation context because several activation rules depend on materiality.

The practitioner artifact may display “Applicable Conditional Profiles A–G / None” as noncanonical completion-aid metadata. That interface aid does not become a schema field.

## Materiality boundary

JSON Schema can validate structure and deterministic relationships. It cannot decide whether a condition is materially significant to a governance determination without additional governance semantics.

Accordingly:

1. the JSON Schema validates the canonical object structure and deterministic cross-field relationships;
2. governance/policy context determines which conditional profiles are materially applicable;
3. the reference validator accepts activated profile IDs externally;
4. field-level materiality triggers remain governed by the approved conditional semantics.

This boundary prevents ordinary telemetry or mere field presence from silently becoming governance materiality.

## Machine scale

The Decision Record is not a one-record-per-model-call design.

One material governance Decision Record may govern or reference many machine-generated execution, telemetry, evidence, or provenance records. Supporting records can be generated at machine scale while governance records are created or escalated at the materiality threshold appropriate to the governed workflow.

The schema supports `HUMAN`, `MACHINE`, and `HYBRID` record generation.

## Repository contents

```text
schema/
  sbj-decision-record.schema.json
rules/
  controlled-enumerations.json
  conditional-profiles.json
  deterministic-cross-field-rules.json
dictionary/
  field-dictionary.json
fixtures/
  valid/A.json ... H.json
  invalid/01-...json ... 10-...json
  valid-manifest.json
  invalid-manifest.json
validator/
  validate.py
docs/
  practitioner-to-schema.md
  practitioner-to-schema.json
  evidence-model.md
  conditional-validation.md
  materiality-and-scale.md
  references.md
```

## Quick start

Requirements:

```bash
python -m pip install jsonschema
```

Validate a record with schema rules only:

```bash
python validator/validate.py fixtures/valid/A.json
```

Validate a record with externally activated profiles:

```bash
python validator/validate.py fixtures/valid/D.json --profiles B,C
```

Expected result:

```text
PASS
```

A minimal valid example is available at `fixtures/valid/A.json`.

## Internal technical conformance

The technical package was tested against the included conformance suite:

- valid fixtures **A–H**: 8 expected PASS outcomes;
- invalid/adversarial fixtures **01–10**: 10 expected FAIL outcomes.

All **18 / 18 expected internal fixture outcomes were reproduced** during technical release validation.

This is **internal technical conformance/validation**. It is not external certification, independent external validation, V2.0 architecture benchmark validation, proof of completeness, proof of regulatory compliance, or proof of universal applicability.

See `VALIDATION-REPORT.md`.

## Practitioner artifact

A practitioner-facing SBJ Decision Record V2.0 artifact maps directly to this technical schema.

Practitioner reference: https://solutionsbyjewel.com/ai-governance/decision-record/sbj-ai-governance-decision-record-v2-practitioner-reference.pdf

Fillable governance template: https://solutionsbyjewel.com/ai-governance/decision-record/sbj-ai-governance-decision-record-v2-template.docx

See `docs/practitioner-to-schema.md` for the field mapping.

## Canonical source

The **Solutions by Jewel website remains the canonical methodology/resource source**. GitHub is the supporting technical/public evidence layer.

Canonical SBJ website artifact URL: **https://solutionsbyjewel.com/ai-governance/decision-record/**.

## External references

This repository includes contextual references to JSON Schema and recognized AI governance sources in `docs/references.md`. Those references do not imply that NIST, ISO, the European Union, any technology vendor, or any other organization developed, approved, certified, validated, or endorsed the SBJ Decision Record.

## IP and use

The SBJ Decision Record, `LOCATE → ASSIGN → RECORD → SCALE`, associated field architecture, conditional-profile structure, and related methodology are original Solutions by Jewel methodology.

See `NOTICE.md` and `LICENSE.md`.

The repository uses the SBJ Technical Reference License 1.0 to preserve SBJ ownership while permitting internal evaluation and implementation. See `LICENSE.md`.

## Contributing

Contributions may address documentation clarity, implementation defects, validator defects, or non-semantic packaging issues. Changes to methodology, canonical fields, controlled values, profile semantics, evidence-sufficiency semantics, guardrails, or schema semantics are outside ordinary contribution scope.

See `CONTRIBUTING.md`.
