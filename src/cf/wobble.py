import numpy as np
def detect_wobble(field, params):
    phases = np.array([n['phase'] for n in field.nodes])
    phase_std = float(np.std(phases))
    clusters = field.anchor_clusters()
    cluster_info = []
    for cl in clusters:
        phases_cl = [n['phase'] for n in cl.nodes]
        cluster_info.append({'id': cl.id, 'phase_std': float(np.std(phases_cl))})
    coherence_mean = max(0.0, 1.0 - phase_std)
    return {'phase_std': phase_std, 'coherence_mean': coherence_mean, 'clusters': cluster_info}
