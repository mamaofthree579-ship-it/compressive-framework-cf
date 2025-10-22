# Compressive Framework (CF) — Simulation & Visualization Scaffold

**Repository name:** compressive-framework-cf  
**Purpose:** Open-source simulation scaffold for the Compressive Framework (CF) — a computational and visualization toolkit for exploring harmonic, geometric, and compressive models in simulation-only contexts.

**Disclaimer:** This repository contains simulation and visualization tools exploring harmonic, geometric, and compressive models as **mathematical and computational experiments**. It does **not** provide verified physical devices or claims of energy generation. Results are simulation-only and intended for open-source research, education, and artistic/scientific visualization. Do not interpret outputs as proven real-world energy extraction methods.

## Quickstart (Python 3.11)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/examples/run_cf_demo.py --config data/examples/run_config_example.json
```

Outputs will appear under `results/` created by the demo.

## Structure
See repository layout in the project root.

## Contributing
Please follow the CONTRIBUTING.md and CODE_OF_CONDUCT.md guidelines.


## Additional features added
- Deterministic RNG usage (numpy default_rng with seed) for reproducible runs.
- Extended wobble diagnostics: subharmonic index and phi-symmetry heuristic.
- Jupyter notebook demo in `notebooks/` that runs the small simulation and saves a plot.
- More anchor clusters in Field and slightly richer initial conditions.
