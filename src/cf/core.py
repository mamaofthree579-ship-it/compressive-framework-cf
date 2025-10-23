import json
import numpy as np
from .arms import ArmModel
from .field import Field
from .field_utils import step_field_phase
from .wobble import detect_wobble
from .autotune import autotune_anchor_clusters

def run_simulation_with_spectral(config, arms_def):
    rng = np.random.default_rng(config.get('seed', 0))
    np.random.seed(config.get('seed', 0))
    arms = [ArmModel(ad['id'], ad['params']) for ad in arms_def['arms']]
    field = Field(config['field']['grid_resolution'], config['field']['initial_density'], rng=rng)
    dt = config['time_step']
    steps = max(1, int(config['total_time'] / dt))
    results = []
    for step in range(steps):
        t = step * dt
        step_field_phase(field, dt, coupling_strength=0.03)
        for arm in arms:
            arm.propagate(field, dt)
        metrics = detect_wobble(field, config['wobble_detection'])
        if config['autotune']['enabled']:
            autotune_anchor_clusters(field.anchor_clusters(), config['wobble_detection']['phase_error_threshold'], config['autotune']['density_delta'], config['autotune']['freq_delta_ratio'], config['autotune']['sync_radius'])
        if step % max(1, config['output']['save_interval']) == 0:
            results.append({'time': t, 'coherence_mean': metrics.get('coherence_mean', 0), 'phase_std': metrics.get('phase_std', 0)})
    return {'results': results, 'metadata': {'seed': config.get('seed',0), 'steps': steps, 'method':'spectral_rk4'}}
