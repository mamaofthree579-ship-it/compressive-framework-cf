\
# Math Reference

Key symbols and heuristic equations used in the scaffold:

- \(\omega_r\) — resonance frequency (ƒr)
- \(\nabla C\) — compression gradient
- \(H_f\) — harmonic feedback coefficient
- \(\phi_i(t)\) — phase of node \(i\)

Discrete phase update (heuristic):
\[\phi_i(t+\Delta t) = \phi_i(t) + \omega_{r,i}\Delta t + H_{f,i}F_i(\{\phi_j\}) + \eta_i(t)\]

Coherence metric:
\[\sigma_\phi = \sqrt{\frac{1}{N}\sum_{i=1}^N (\phi_i - \bar\phi)^2},\quad \mathrm{coherence}=\max(0,1-\sigma_\phi)\]
