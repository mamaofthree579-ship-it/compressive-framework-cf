def step_field_phase(field, dt, coupling_strength=0.05):
    import numpy as np
    from .spectral import spectral_coupling_matrix, rk4_step
    phases = np.array([n['phase'] for n in field.nodes])
    omega_r = 1.0
    coupling = lambda p: spectral_coupling_matrix(p, coupling_strength)
    new_phases = rk4_step(phases, omega_r, coupling, dt)
    for idx, n in enumerate(field.nodes):
        n['phase'] = float(new_phases[idx])
