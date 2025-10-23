import numpy as np
from typing import List
class AnchorCluster:
    def __init__(self, id, density=1.0, resonance_frequency=1.0, nodes=None):
        self.id = id
        self.density = density
        self.resonance_frequency = resonance_frequency
        self.nodes = nodes or []

    def measure_local_phase_error(self):
        if not self.nodes:
            return 0.0
        phases = np.array([n['phase'] for n in self.nodes])
        return float(np.std(phases))

    def sync_with(self, other):
        self.density = 0.5*(self.density + other.density)
        self.resonance_frequency = 0.5*(self.resonance_frequency + other.resonance_frequency)

class Field:
    def __init__(self, grid_resolution=32, initial_density=1.0, rng=None):
        self.grid_resolution = grid_resolution
        self.nodes = []
        self.rng = rng
        N = grid_resolution * grid_resolution
        for i in range(N):
            phase = float(rng.normal(0,0.001)) if rng is not None else 0.0
            self.nodes.append({'phase': phase, 'density': initial_density})
        split = max(1, N//10)
        self._anchor_clusters = []
        for idx, label in enumerate(['A','B','C']):
            start = idx*split
            end = min((idx+1)*split, N)
            nodes_slice = self.nodes[start:end]
            self._anchor_clusters.append(AnchorCluster(label, density=1.0, resonance_frequency=1.0 + idx*0.02, nodes=nodes_slice))

    def add_phase_noise(self, delta):
        for n in self.nodes:
            noise = float(self.rng.normal(0, delta*0.1)) if self.rng is not None else 0.0
            n['phase'] += delta + noise

    def anchor_clusters(self) -> List[AnchorCluster]:
        return self._anchor_clusters
