import numpy as np
import plotly.graph_objects as go

fig = go.Figure()

x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)

x, y = np.meshgrid(x, y)

z = np.sqrt(x**2 + y**2)

fig.add_trace(go.Surface(
    x=x,
    y=y,
    z=z,
    colorscale='Greens', opacity=0.7, showscale=False
))

fig.update_layout(
    title="Right Circular Cone",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
        xaxis=dict(range=[-2, 2]),
        yaxis=dict(range=[-2, 2]),
        zaxis=dict(range=[0, 1]),
    )
)

fig.write_html("right_circular_cone.html")
