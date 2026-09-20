# SBJ AI Governance Decision Record V2.0 — Technical Schema 2.0.0

This release packages the frozen SBJ Decision Record V2.0 as a machine-readable technical reference for AI governance teams, engineers, architects, risk and compliance teams, security teams, internal audit, AI platform teams, and governance automation developers.

## Included

- JSON Schema Draft 2020-12: `urn:sbj:decision-record:schema:2.0.0`
- controlled-enumeration definitions
- conditional profiles A–G
- deterministic cross-field validation rules
- reference validator
- valid fixtures A–H
- invalid/adversarial fixtures 01–10
- machine-readable field dictionary
- practitioner-to-schema mapping
- implementation documentation

## Methodology

`LOCATE → ASSIGN → RECORD → SCALE`

## Internal technical conformance

The included technical suite reproduced 18 / 18 expected internal fixture outcomes: eight valid fixtures passed and ten invalid/adversarial fixtures failed as expected.

This is internal technical conformance/validation. It is not external certification, independent external validation, V2.0 architecture benchmark validation, proof of completeness, proof of regulatory compliance, or proof of universal applicability.

## Evidence architecture

The release uses a reference-first evidence model. Evidence and telemetry remain external; the Decision Record references authoritative evidence when material. Evidence existence does not establish evidence sufficiency.

## Conditional validation

Profile activation remains external governance/policy context. The canonical Decision Record JSON object does not contain a profile-membership field.

## Canonical resource

The Solutions by Jewel website remains the canonical methodology/resource destination. Final canonical and practitioner download URLs will be inserted before publication.
