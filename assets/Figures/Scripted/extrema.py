import numpy as np
import plotly.graph_objects as go

fig = go.Figure()

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

x, y = np.meshgrid(x, y)
z = 2 + 2 * x + 2 * y - x**2 - y**2


def domain_plane():
    X = [0, 9, 0]
    Y = [0, 0, 9]
    Z = [0, 0, 0]

    return go.Mesh3d(
        x=X,
        y=Y,
        z=Z,
        color="lightblue",
        opacity=0.7
    )


fig.add_trace(go.Surface(
    x=x,
    y=y,
    z=z,
    colorscale="Greens",
    opacity=0.7,
    showscale=False
))

fig.add_trace(domain_plane())

fig.update_layout(
    title="Extrema",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 10]),
        zaxis=dict(range=[0, 10])
    )
)

fig.write_html("extrema.html")
