import numpy as np
from .base import EquationModel

class ResonanceEquation(EquationModel):
    """Simple resonance model: returns a harmonic response.

    evaluate(frequency, amplitude, phase_offset=0.0, t=None)
    - frequency: scalar or array (Hz)
    - amplitude: scalar
    - phase_offset: radians
    - t: time array (optional). If None, returns scalar amplitude*sin(phase_offset).
    """
    def __init__(self, name='resonance'):
        super().__init__(name)

    def evaluate(self, frequency=1.0, amplitude=1.0, phase_offset=0.0, t=None):
        if t is None:
            return amplitude * np.sin(phase_offset)
        t = np.asarray(t)
        return amplitude * np.sin(2.0 * np.pi * frequency * t + phase_offset)
