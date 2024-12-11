import plotly.graph_objects as go
import numpy as np

# Define the range for the axes
range_vals = np.linspace(-10, 10, 50)

# Create the yz-plane at x = 0
yz_plane_x = np.zeros((50, 50))  # x = 0 for yz-plane
yz_plane_y, yz_plane_z = np.meshgrid(range_vals, range_vals)

# Create the xz-plane at y = 0
xz_plane_y = np.zeros((50, 50))  # y = 0 for xz-plane
xz_plane_x, xz_plane_z = np.meshgrid(range_vals, range_vals)

# Create the xy-plane at z = 0
xy_plane_z = np.zeros((50, 50))  # z = 0 for xy-plane
xy_plane_x, xy_plane_y = np.meshgrid(range_vals, range_vals)

# Create figure
fig = go.Figure()

# Add the yz-plane (x = 0)
fig.add_trace(go.Surface(x=yz_plane_x, y=yz_plane_y, z=yz_plane_z,
              colorscale='Blues', opacity=0.7, showscale=False))

# Add the xz-plane (y = 0)
fig.add_trace(go.Surface(x=xz_plane_x, y=xz_plane_y, z=xz_plane_z,
              colorscale='Reds', opacity=0.7, showscale=False))

# Add the xy-plane (z = 0)
fig.add_trace(go.Surface(x=xy_plane_x, y=xy_plane_y, z=xy_plane_z,
              colorscale='Greens', opacity=0.7, showscale=False))
fig.add_trace(go.Scatter3d(
    x=[5, -5, -5, 5, 5, -5, -5, 5],
    y=[5, 5, -5, -5, 5, 5, -5, -5],
    z=[5, 5, 5, 5, -5, -5, -5, -5],
    mode='text',
    # The text to display at each point
    text=['Octant 1', 'Octant 2', 'Octant 3', 'Octant 4',
          'Octant 5', 'Octant 6', 'Octant 7', 'Octant 8'],
    textposition='top center',  # Position of text relative to the points
    textfont=dict(size=14, color='black')  # Font size and color
))

# Update layout
fig.update_layout(
    title="Interactive 3D Space with Planes x=0, y=0, z=0",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        xaxis=dict(range=[-10, 10]),
        yaxis=dict(range=[-10, 10]),
        zaxis=dict(range=[-10, 10]),
    )
)

# Show figure
fig.write_html("octants.html")
