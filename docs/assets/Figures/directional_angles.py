import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)
z = np.linspace(0, 5, 20)

fig = go.Figure(go.Surface(
    x=x,
    y=y,
    z=z
))

fig.add_trace(
    go.Scatter3d(
        x=[0, 3],
        y=[0, 3],
        z=[0, 3],
        mode="lines",
        line=dict(
            color="blue",
            width=1
        ),
        name="line"
    )
)

fig.add_trace(
    go.Scatter3d(
        x=[0, 3],
        y=[0, 0],
        z=[0, 3],
        mode="lines",
        line=dict(
            color="black",
            width=1
        ),
        name="xy plane"
    )
)

fig.add_trace(
    go.Scatter3d(
        x=[0, 0],
        y=[0, 3],
        z=[0, 3],
        mode="lines",
        line=dict(
            color="black",
            width=1
        ),
        name="yz plane"
    )
)

fig.add_trace(
    go.Scatter3d(
        x=[0, 3],
        y=[0, 3],
        z=[0, 0],
        mode="lines",
        line=dict(
            color="black",
            width=1
        ),
        name="xz plane"
    )
)

fig.update_layout(
    title="Directional angles",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z"
    )
)

fig.write_html("directional_angles.html")
