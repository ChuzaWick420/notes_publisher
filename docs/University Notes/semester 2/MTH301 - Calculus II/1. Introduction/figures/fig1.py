import numpy as np
import plotly.graph_objects as go

# Create data for the paraboloid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = x**2 + y**2  # Equation of the paraboloid

# Create the figure
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Update plot layout
fig.update_layout(title='Interactive Paraboloid', scene=dict(
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    zaxis_title='Z Axis'
))

# Save the plot as an HTML file
fig.write_html("paraboloid_plot.html")
