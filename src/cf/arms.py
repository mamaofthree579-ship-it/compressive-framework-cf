class ArmModel:
    def __init__(self, id, params):
        self.id = id
        self.base_frequency = params.get('base_frequency', 1.0)
        self.damping = params.get('damping', 0.01)
    def propagate(self, field, dt):
        # simple nudge
        field.add_phase_noise(self.base_frequency * dt * 0.001)
