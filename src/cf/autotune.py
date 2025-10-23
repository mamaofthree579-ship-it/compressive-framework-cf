def autotune_anchor_clusters(clusters, phase_threshold, density_delta, freq_delta_ratio, sync_radius):
    for cl in clusters:
        err = cl.measure_local_phase_error()
        if err > phase_threshold:
            cl.density = max(0.001, cl.density - abs(density_delta))
    return clusters
