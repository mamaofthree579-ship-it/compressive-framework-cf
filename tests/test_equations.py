import numpy as np
from cf.equations.registry import EQUATION_REGISTRY, list_equations

def test_registry_keys():
    keys = list_equations()
    assert 'resonance' in keys
    assert 'compression' in keys
    assert 'feedback' in keys

def test_resonance_basic():
    eq = EQUATION_REGISTRY['resonance']
    t = np.linspace(0, 1, 50)
    out = eq.evaluate(frequency=2.0, amplitude=0.5, t=t)
    assert out.shape == t.shape
    # values should be bounded by amplitude
    assert np.all(np.abs(out) <= 0.5 + 1e-12)

def test_compression_scaling():
    eq = EQUATION_REGISTRY['compression']
    out = eq.evaluate(base_frequency=1.0, compression=0.2, alpha=0.5)
    assert abs(out - 1.1) < 1e-8

def test_feedback_stability():
    eq = EQUATION_REGISTRY['feedback']
    phases = np.zeros(10)
    out = eq.evaluate(phases, hf=0.0)
    assert np.allclose(out, 0.0)
