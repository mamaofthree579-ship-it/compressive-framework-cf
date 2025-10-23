import numpy as np
import plotly.graph_objects as go

def visualize_waveform(x, y, title="Harmonic Field"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines"))
    fig.update_layout(title=title, xaxis_title="x", yaxis_title="Amplitude")
    fig.show()
