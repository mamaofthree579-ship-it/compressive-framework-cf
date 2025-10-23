import numpy as np
from .base import EquationModel

class CompressionEquation(EquationModel):
    """Model a simple compression-to-frequency mapping.

    Example: frequency scales with (1 + alpha * compression)
    evaluate(base_frequency, compression, alpha=0.1)
    """
    def __init__(self, name='compression'):
        super().__init__(name)

    def evaluate(self, base_frequency=1.0, compression=0.0, alpha=0.1):
        base = np.asarray(base_frequency)
        comp = np.asarray(compression)
        return base * (1.0 + alpha * comp)
