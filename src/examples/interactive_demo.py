"""Interactive demo: runs small simulation and produces an interactive Plotly HTML snapshot.
Requires plotly installed (included in requirements.txt).
"""
import json, os
import numpy as np
from cf.core import run_simulation_with_spectral
from cf.export import save_run_metadata, save_field_snapshot, export_summary_html
try:
    import plotly.graph_objs as go
    import plotly.offline as pyo
except Exception:
    go = None; pyo = None

def run_demo(config_path='data/examples/run_config_example.json'):
    with open(config_path) as fh:
        cfg = json.load(fh)
    arms = json.load(open('data/examples/arm_definitions.json'))
    out = run_simulation_with_spectral(cfg, arms)
    outdir = cfg['output']['output_dir']
    os.makedirs(outdir, exist_ok=True)
    save_run_metadata(out['metadata'], outdir)
    # create a Field and step once to get state
    from cf.field import Field
    field = Field(cfg['field']['grid_resolution'], cfg['field']['initial_density'], rng=np.random.default_rng(cfg.get('seed',0)))
    from cf.field_utils import step_field_phase
    step_field_phase(field, cfg['time_step'], coupling_strength=0.03)
    save_field_snapshot(field, outdir, name='interactive')
    export_summary_html(outdir, out)
    if pyo is not None:
        nodes = field.nodes
        N = len(nodes)
        side = int(cfg['field']['grid_resolution'])
        xs = [i % side for i in range(N)]
        ys = [i // side for i in range(N)]
        phases = [n['phase'] for n in nodes]
        scatter = go.Scattergl(x=xs, y=ys, mode='markers', marker=dict(size=6, color=phases, colorscale='Viridis', showscale=True), text=[f'phase: {p:.4f}' for p in phases])
        fig = go.Figure(data=[scatter])
        out_html = os.path.join(outdir, 'interactive_field.html')
        pyo.plot(fig, filename=out_html, auto_open=False)
        print('Wrote interactive HTML to', out_html)
    else:
        print('Plotly not available, exported numeric snapshots to', outdir)

if __name__ == '__main__':
    run_demo()
