import numpy as np
from cf.wobble import compute_subharmonic_index, phi_symmetry_score
def test_subharmonic_index_basic():
    # create a signal with a strong subharmonic component
    t = np.linspace(0,1,128)
    sig = np.sin(2*np.pi*2*t) + 0.5*np.sin(2*np.pi*1*t)
    idx = compute_subharmonic_index(sig, base_freq=2.0)
    assert idx > 0
def test_phi_symmetry_basic():
    t = np.linspace(0,1,128)
    sig = np.sin(2*np.pi*1.618*t) + 0.2*np.sin(2*np.pi*3.3*t)
    score = phi_symmetry_score(sig)
    assert 0 <= score <= 1
