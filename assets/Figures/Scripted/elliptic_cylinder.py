import numpy as np
import plotly.graph_objects as go

fig = go.Figure()


def cylinder(r, h, points=200):

    theta = np.linspace(0, 2*np.pi, points)
    v = np.linspace(0, h, points)
    theta, v = np.meshgrid(theta, v)

    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = v

    return x, y, z


X, Y, Z = cylinder(3, 10)

fig.add_trace(go.Surface(
    x=X,
    y=Y,
    z=Z,
    colorscale='Blues', opacity=0.7, showscale=False
))

fig.update_layout(
    title="Elliptic Cylinder",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=[-10, 10]),
        zaxis=dict(range=[0, 10]),
    )
)

fig.write_html("elliptic_cylinder.html")
