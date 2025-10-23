def autotune_anchor_clusters(clusters, phase_threshold, density_delta, freq_delta_ratio, sync_radius):
    for cl in clusters:
        err = cl.measure_local_phase_error()
        if err > phase_threshold:
            cl.density = max(0.001, cl.density - abs(density_delta))
            cl.resonance_frequency += (1 if err>0 else -1) * (freq_delta_ratio * abs(density_delta))
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            clusters[i].sync_with(clusters[j])
            clusters[j].sync_with(clusters[i])
    return clusters
