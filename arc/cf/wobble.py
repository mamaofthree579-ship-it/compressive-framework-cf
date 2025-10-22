import numpy as np
def compute_subharmonic_index(phases, base_freq=1.0):
    """Compute a simple subharmonic index:
    ratio of energy in subharmonic bands (e.g., 1/2, 1/3) vs base band.
    Here we approximate via FFT power ratios for demo purposes.
    """
    if len(phases) < 4:
        return 0.0
    # windowed FFT
    vals = np.array(phases)
    fft = np.fft.rfft(vals - np.mean(vals))
    psd = np.abs(fft)**2
    freqs = np.fft.rfftfreq(len(vals), d=1.0)  # assume unit sampling
    # find index of base band (closest to base_freq)
    idx_base = (np.abs(freqs - base_freq)).argmin()
    # look for subharmonics at base/2, base/3
    idx_sub2 = (np.abs(freqs - base_freq/2)).argmin()
    idx_sub3 = (np.abs(freqs - base_freq/3)).argmin()
    sub_energy = psd[idx_sub2] + psd[idx_sub3]
    base_energy = psd[idx_base] + 1e-12
    return float(sub_energy / base_energy)

def phi_symmetry_score(phases):
    """Check for golden-ratio-like harmonic locking by comparing
    ratios of dominant frequencies. This is a heuristic demo only.
    Returns a score in [0,1], higher means closer to phi-related ratios.
    """
    if len(phases) < 4:
        return 0.0
    vals = np.array(phases)
    fft = np.fft.rfft(vals - np.mean(vals))
    psd = np.abs(fft)**2
    freqs = np.fft.rfftfreq(len(vals), d=1.0)
    # pick top two frequency peaks (excluding DC)
    psd[0] = 0
    top_idx = np.argsort(psd)[-2:]
    if len(top_idx) < 2:
        return 0.0
    f1, f2 = freqs[top_idx[0]], freqs[top_idx[1]]
    ratio = max(f1,f2) / (min(f1,f2) + 1e-12)
    phi = 1.61803398875
    # score based on closeness to phi or its powers
    score = max(0.0, 1.0 - abs(ratio - phi) / phi)
    return float(score)

def detect_wobble(field, params):
    # simple metric: compute std of phases across all nodes
    phases = np.array([n['phase'] for n in field.nodes])
    phase_std = float(np.std(phases))
    # compute per-cluster diagnostics
    clusters = field.anchor_clusters()
    cluster_info = []
    for cl in clusters:
        phases_cl = [n['phase'] for n in cl.nodes]
        sub_idx = compute_subharmonic_index(phases_cl, base_freq=1.0)
        phi_score = phi_symmetry_score(phases_cl)
        cluster_info.append({'id': cl.id, 'phase_std': float(np.std(phases_cl)),
                             'subharmonic_index': sub_idx, 'phi_score': phi_score})
    coherence_mean = max(0.0, 1.0 - phase_std)
    return {'phase_std': phase_std, 'coherence_mean': coherence_mean, 'clusters': cluster_info}
