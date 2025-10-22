import numpy as np
from cf.autotune import autotune_anchor_clusters
from cf.field import AnchorCluster
def test_autotune_reduces_density():
    cl1 = AnchorCluster('t1', density=1.0, resonance_frequency=1.0, nodes=[{'phase':0.0},{'phase':0.2}])
    cl2 = AnchorCluster('t2', density=1.0, resonance_frequency=1.0, nodes=[{'phase':0.0},{'phase':0.1}])
    clusters = [cl1, cl2]
    updated = autotune_anchor_clusters(clusters, phase_threshold=0.05, density_delta=0.1, freq_delta_ratio=0.5, sync_radius=1)
    assert updated[0].density < 1.0 or updated[1].density < 1.0
