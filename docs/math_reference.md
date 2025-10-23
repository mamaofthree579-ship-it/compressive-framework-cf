\
# Math Reference — Equation API

This page describes the equation API and the example models included in the `cf.equations` package.

## EquationModel (base)
All model classes inherit from `EquationModel` and implement:

```python
def evaluate(self, *args, **kwargs):
    ...
```

They should accept numpy arrays and return numpy arrays or scalars.

## Included equation models
- `resonance`: `evaluate(frequency, amplitude, phase_offset=0.0, t=None)`
- `compression`: `evaluate(base_frequency, compression, alpha=0.1)`
- `feedback`: `evaluate(phases, hf=0.1, neighbor_kernel=None)`

These are lightweight, testable building blocks intended as starting points for more complex physics modules.
