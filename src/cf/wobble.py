import numpy as np
def detect_wobble(field, params):
    phases = np.array([n['phase'] for n in field.nodes])
    phase_std = float(np.std(phases))
    return {'phase_std': phase_std, 'coherence_mean': max(0.0,1.0-phase_std)}
