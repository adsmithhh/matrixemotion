# EMX — Emotional Mixing Matrix

EMX is an open-source, lightweight, and interoperable engine and matrix format for modeling, mixing, and evolving emotions in AI agents, NPCs, simulations, and games.

## Scientific Background

Based on Dr. Robert Plutchik's theory, EMX models eight primary emotions as the foundation for all others:

- **Joy**
- **Sadness**
- **Acceptance**
- **Disgust**
- **Fear**
- **Anger**
- **Surprise**
- **Anticipation**

By representing these emotions as a matrix, EMX enables complex, dynamic, and realistic emotional states for autonomous agents.

## Features

- Interoperable matrix format + reference engine
- Deterministic core with pluggable heuristics
- Safety-aware (caps, inhibitors, guards)
- Apache-2.0 licensed
- Quick start, minimal dependencies

## Quick Start

```sh
pip install pyyaml
PYTHONPATH=. python examples/run_step.py
```

## Example

```yaml
# Input emotion matrix
emotions:
  joy: 0.7
  sadness: 0.1
  anger: 0.1
  fear: 0.1
```
```sh
# Run a processing step
python examples/run_step.py
```
```yaml
# Output (example)
emotions:
  joy: 0.65
  sadness: 0.15
  anger: 0.10
  fear: 0.10
```

## Contributing

We welcome contributions of all kinds! Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[Apache-2.0](LICENSE)

---

*Built and maintained by ropentimer-[@adsmithhh](https://github.com/adsmithhh).*