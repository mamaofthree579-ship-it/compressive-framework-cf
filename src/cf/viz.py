import matplotlib.pyplot as plt
def plot_timeseries(times, values, outpath):
    plt.figure()
    plt.plot(times, values)
    plt.xlabel('time (s)')
    plt.ylabel('coherence_mean')
    plt.title('CF demo: coherence over time')
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
