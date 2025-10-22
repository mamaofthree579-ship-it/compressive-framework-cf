import time
import json
import numpy as np
from .arms import ArmModel
from .field import Field
from .wobble import detect_wobble
from .autotune import autotune_anchor_clusters

def run_simulation(config, arms_def):
    rng = np.random.default_rng(config.get('seed', 0))
    # set numpy global seed for deterministic behaviors used by older code paths
    np.random.seed(config.get('seed', 0))
    arms = [ArmModel(ad['id'], ad['params']) for ad in arms_def['arms']]
    field = Field(config['field']['grid_resolution'], config['field']['initial_density'], rng=rng)
    dt = config['time_step']
    steps = max(1, int(config['total_time'] / dt))
    results = []
    for step in range(steps):
        t = step * dt
        for arm in arms:
            arm.propagate(field, dt)
        metrics = detect_wobble(field, config['wobble_detection'])
        if config['autotune']['enabled']:
            autotune_anchor_clusters(field.anchor_clusters(), config['wobble_detection']['phase_error_threshold'],
                                     config['autotune']['density_delta'], config['autotune']['freq_delta_ratio'],
                                     config['autotune']['sync_radius'])
        if step % max(1, config['output']['save_interval']) == 0:
            results.append({'time': t, 'coherence_mean': metrics.get('coherence_mean', 0),
                            'phase_std': metrics.get('phase_std', 0)})
    return {'results': results, 'metadata': {'seed': config.get('seed',0), 'steps': steps}}

def main(config_path):
    with open(config_path) as fh:
        cfg = json.load(fh)
    with open('data/examples/arm_definitions.json') as fh:
        arms_def = json.load(fh)
    out = run_simulation(cfg, arms_def)
    res = out['results']
    # save a simple CSV
    import csv
    outdir = cfg['output']['output_dir']
    import os
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'timeseries.csv'),'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['time','coherence_mean','phase_std'])
        writer.writeheader()
        for r in res:
            writer.writerow(r)
    # save metadata
    with open(os.path.join(outdir, 'metadata.json'),'w') as mfh:
        json.dump(out['metadata'], mfh, indent=2)
    print('Simulation complete. Results saved to:', outdir)
