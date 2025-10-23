import json, os
def save_run_metadata(metadata, outdir):
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'metadata.json'),'w') as fh:
        json.dump(metadata, fh, indent=2)

def save_field_snapshot(field, outdir, name='snapshot'):
    import numpy as np, os, csv
    os.makedirs(outdir, exist_ok=True)
    phases = [n['phase'] for n in field.nodes]
    np.save(os.path.join(outdir, f'{name}_phases.npy'), phases)
    with open(os.path.join(outdir, f'{name}_summary.csv'),'w',newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(['index','phase'])
        for i,p in enumerate(phases):
            writer.writerow([i, p])

def export_summary_html(outdir, summary, filename='summary.html'):
    import os
    os.makedirs(outdir, exist_ok=True)
    html = '<html><body><h1>Run Summary</h1><pre>' + (str(summary)) + '</pre></body></html>'
    with open(os.path.join(outdir, filename),'w') as fh:
        fh.write(html)
