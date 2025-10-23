import numpy as np
from .base import EquationModel

class FeedbackEquation(EquationModel):
    """Simple harmonic feedback model.

    evaluate(phases, hf=0.1, neighbor_kernel=None)
    - phases: 1D array of node phases
    - hf: feedback coefficient
    - neighbor_kernel: optional array of same length for weighted neighbors
    Returns: array of feedback adjustments (same shape as phases)
    """
    def __init__(self, name='feedback'):
        super().__init__(name)

    def evaluate(self, phases, hf=0.1, neighbor_kernel=None):
        phases = np.asarray(phases)
        if neighbor_kernel is None:
            # simple nearest-neighbor average based on roll
            left = np.roll(phases, 1)
            right = np.roll(phases, -1)
            mean_neighbor = 0.5*(left + right)
        else:
            kernel = np.asarray(neighbor_kernel)
            mean_neighbor = kernel * phases
        return hf * np.sin(mean_neighbor - phases)
