import numpy as np
class AnchorCluster:
    def __init__(self,id,density=1.0,resonance_frequency=1.0,nodes=None):
        self.id=id; self.density=density; self.resonance_frequency=resonance_frequency; self.nodes=nodes or []
    def measure_local_phase_error(self):
        import numpy as np
        if not self.nodes: return 0.0
        return float(np.std([n['phase'] for n in self.nodes]))
    def sync_with(self,other):
        self.density=0.5*(self.density+other.density); self.resonance_frequency=0.5*(self.resonance_frequency+other.resonance_frequency)
class Field:
    def __init__(self,grid_resolution=32,initial_density=1.0,rng=None):
        self.grid_resolution=grid_resolution; self.rng=rng
        N=grid_resolution*grid_resolution
        self.nodes=[{'phase': float(rng.normal(0,0.001)) if rng is not None else 0.0, 'density':initial_density} for _ in range(N)]
        split=max(1,N//10)
        self._anchor_clusters=[]
        for idx,label in enumerate(['A','B','C']):
            start=idx*split; end=min((idx+1)*split,N)
            self._anchor_clusters.append(AnchorCluster(label,nodes=self.nodes[start:end]))
    def add_phase_noise(self,delta):
        import numpy as np
        for n in self.nodes:
            n['phase'] += (self.rng.normal(0,delta*0.1) if self.rng is not None else 0.0) + delta
    def anchor_clusters(self):
        return self._anchor_clusters
