import numpy as np

def spectral_coupling_matrix(phases, coupling_strength=0.1):
    vals = np.array(phases)
    fft = np.fft.rfft(np.exp(1j * vals))
    cutoff = max(1, int(len(fft)*0.1))
    fft[cutoff:] = 0
    smoothed = np.fft.irfft(fft, n=len(vals))
    avg_phase = np.angle(smoothed)
    coupling = coupling_strength * np.sin(avg_phase - vals)
    return coupling

def rk4_step(phases, omega_r, coupling_func, dt):
    import numpy as np
    def deriv(p):
        return omega_r + coupling_func(p)
    k1 = deriv(phases)
    k2 = deriv(phases + 0.5*dt*k1)
    k3 = deriv(phases + 0.5*dt*k2)
    k4 = deriv(phases + dt*k3)
    return phases + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)
