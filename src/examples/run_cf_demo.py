import argparse, json, os
from cf.core import main
from cf.viz import plot_timeseries
import csv

def run_demo(config_path):
    main(config_path)
    # quick plot if timeseries exists
    cfg = json.load(open(config_path))
    outdir = cfg['output']['output_dir']
    csvpath = os.path.join(outdir, 'timeseries.csv')
    if os.path.exists(csvpath):
        times, vals = [], []
        with open(csvpath) as fh:
            reader = csv.DictReader(fh)
            for r in reader:
                times.append(float(r['time']))
                vals.append(float(r['coherence_mean']))
        plot_timeseries(times, vals, os.path.join(outdir, 'coherence.png'))
        print('Plot saved to', os.path.join(outdir, 'coherence.png'))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--config', default='data/examples/run_config_example.json')
    args = p.parse_args()
    run_demo(args.config)
