# EMX — Emotional Mixing Matrix (Open Source)

EMX is a lightweight, interoperable **emotional mixing matrix** format and reference engine
for autonomous AI agents. It standardizes how emotions are represented, mixed, and evolved
over time in simulations, dialogue systems, and game AIs.

## Why EMX?
- **Interoperable:** One matrix format for many engines.
- **Deterministic core, pluggable heuristics:** Reproducible results with optional modules.
- **Safety-aware fields:** Built-in inhibitors, caps, and guards.
- **Open license (Apache-2.0).**

> Core idea: represent an emotion vector `E ∈ R^n` and a coupling tensor `W ∈ R^{n×n}`,
> step the system with decay, bounds, and non-linearities.

## Quick Start (Python)
```bash
pip install -e .
python examples/run_step.py
```

## Format Overview
- `schema/emx.schema.json` — JSON Schema for validation
- `examples/base.yaml` — 8-emotion base (Plutchik-style) with couplings
- `examples/policy.yaml` — safety/negation operators and guards
- `emx/engine.py` — minimal deterministic engine (forward Euler)
- `emx/io.py` — load/validate (YAML/JSON)
- `tests/test_engine.py` — sanity checks

## Versioning
`emx_version: "0.1.0"` in every file. Semantic versioning.
Breaking changes bump the minor/major.

## Safety & Operators
- **caps**: per-emotion hard limits.
- **inhibitors**: (0–1) multipliers to damp selected routes.
- **isnt_operator**: hard negation of recent clause (¬A) with conflict resolution rules.
- **zero_equals_one_probe**: optional symbolic-probe flag to log contradiction surfaces.

See `examples/policy.yaml` for usage.

## License
Apache-2.0. See `LICENSE`.
