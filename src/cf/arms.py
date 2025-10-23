class ArmModel:
    def __init__(self,id,params):
        self.id=id
        self.base_frequency=params.get('base_frequency',1.0)
    def propagate(self,field,dt):
        field.add_phase_noise(0.0)
