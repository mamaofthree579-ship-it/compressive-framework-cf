import numpy as np

class ArmModel:
    def __init__(self, id, params):
        self.id = id
        self.base_frequency = params.get('base_frequency', 1.0)
        self.damping = params.get('damping', 0.01)

    def propagate(self, field, dt):
        # simplistic propagation: nudge field phases by a small oscillation
        phase_shift = self.base_frequency * dt * (1.0 - self.damping)
        field.add_phase_noise(phase_shift * 0.001)
