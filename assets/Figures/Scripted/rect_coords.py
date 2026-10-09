import numpy as np
import plotly.graph_objects as go

fig = go.Figure()


def plane(x_offset, y_offset, z_offset, normal_to_axis='z'):
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    z = np.linspace(-5, 5, 50)

    if (normal_to_axis == 'z'):
        x, y = np.meshgrid(x, y)
        z = np.zeros_like(x) + z_offset
        x = x + x_offset
        y = y + y_offset
    elif (normal_to_axis == 'x'):
        z, y = np.meshgrid(z, y)
        x = np.zeros_like(z) + x_offset
        y = y + y_offset
        z = z + z_offset
    elif (normal_to_axis == 'y'):
        z, x = np.meshgrid(z, x)
        y = np.zeros_like(x) + y_offset
        z = z + z_offset
        x = x + x_offset

    return go.Surface(
        x=x,
        y=y,
        z=z,
        colorscale="Blues",
        opacity=0.7,
        showscale=False
    )


fig.add_trace(plane(0, 0, 5))
fig.add_trace(plane(0, 0, -5))
fig.add_trace(plane(5, 0, 0, 'x'))
fig.add_trace(plane(-5, 0, 0, 'x'))
fig.add_trace(plane(0, 5, 0, 'y'))
fig.add_trace(plane(0, -5, 0, 'y'))

fig.add_trace(go.Scatter3d(
    x=[5],
    y=[5],
    z=[5],
    mode="markers",
    marker=dict(
        color="Red",
        size=8
    )
))

fig.update_layout(
    title="Rectangular Coordinates",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
        xaxis=dict(range=[-5, 10]),
        yaxis=dict(range=[-5, 10]),
        zaxis=dict(range=[-5, 10])
    )
)

fig.write_html("rect_coords.html")
