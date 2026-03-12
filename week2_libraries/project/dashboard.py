import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load data
url = "https://raw.githubusercontent.com/datamole-ai/edvart/refs/heads/main/example-datasets/auto.csv"
data = pd.read_csv(url)

# Handle missing values
data['mpg'] = data['mpg'].fillna(data['mpg'].mean())

# Create Dash application
app = Dash(__name__)

# Create interactive scatter plot
# Correcting usage: pass dataframe as first arg, map columns to x, y, size.
# Using 'skyblue' for all points requires update_traces or color_discrete_sequence.
fig = px.scatter(
    data,
    x='displacement',
    y='acceleration',
    size='mpg',
    hover_data=['weight', 'horsepower'],
    title="Displacement vs Acceleration by MPG"
)

# Apply the skyblue color to markers
fig.update_traces(marker=dict(color='skyblue'))

# Define layout
app.layout = html.Div([
    html.H1("Auto Dataset Dashboard", style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(figure=fig)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
