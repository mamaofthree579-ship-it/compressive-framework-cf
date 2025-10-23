import matplotlib.pyplot as plt
def plot_timeseries(times, values, outpath):
    plt.figure(); plt.plot(times, values); plt.savefig(outpath); plt.close()
