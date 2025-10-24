# scripts/generate_reference_plot.py
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

def psi(x, t, A=1.0, k=2*np.pi/5, w=2*np.pi/3, a=0.1):
    return A * np.sin(k * x - w * t) * np.exp(-a * x)

def main():
    out_dir = Path("docs/images")
    out_dir.mkdir(parents=True, exist_ok=True)

    x = np.linspace(0, 20, 800)
    t_snapshot = 2.0
    params = dict(A=1.0, k=2*np.pi/5, w=2*np.pi/3, a=0.1)

    y = psi(x, t_snapshot, **params)

    plt.figure(figsize=(10,4.5), dpi=120)
    plt.plot(x, y, lw=1.8)
    plt.title("CF Harmonic Compression — reference snapshot (t=2.0)")
    plt.xlabel("x")
    plt.ylabel("Ψ(x,t)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    out_file = out_dir / "reference_snapshot.png"
    plt.savefig(out_file)
    print("Saved reference plot to", out_file)

if __name__ == "__main__":
    main()
