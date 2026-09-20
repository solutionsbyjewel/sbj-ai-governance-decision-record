# Contributing

The public repository is a technical implementation of a frozen SBJ Decision Record specification.

## In scope

Contributions may propose:

- documentation corrections or clarity improvements;
- validator implementation defects;
- test-harness defects;
- non-semantic packaging corrections;
- reproducibility improvements that do not alter the frozen schema semantics.

## Out of scope for ordinary contribution

Pull requests must not redesign or silently modify:

- `LOCATE → ASSIGN → RECORD → SCALE`;
- the nine-field canonical core;
- field semantics;
- controlled values;
- conditional-profile semantics;
- evidence-sufficiency semantics;
- VE01 / VE02 / VE03 guardrails;
- materiality boundaries;
- deterministic validation semantics.

Proposals affecting those areas require separate Solutions by Jewel architecture/methodology adjudication before implementation.

## Security and secrets

Do not submit records containing passwords, tokens, API keys, private keys, regulated production data, or other secrets. Use synthetic or sanitized examples.
