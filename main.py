from flask import Flask
import os
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Create Flask server first
server = Flask(__name__)

# Pass the Flask server to Dash
app = Dash(__name__, server=server)

# Mock live data (upgrade to real APIs later)
climate_risk = 8.7
conflict_events = 45
disease_outbreaks = 12

# Dashboard layout
app.layout = html.Div(style={
    'backgroundColor': '#000',
    'color': '#0f0',
    'fontFamily': 'monospace',
    'textAlign': 'center'
}, children=[
    html.H1("NEXUS SENTINEL", style={'fontSize': '4rem', 'textShadow': '0 0 20px #0f0'}),
    html.H2("Climate • Conflict • Disease Intelligence Platform", style={'color': '#0ff'}),
    
    dcc.Graph(figure=px.bar(
        x=['CLIMATE', 'CONFLICT', 'DISEASE'],
        y=[climate_risk, conflict_events // 5, disease_outbreaks],
        color=[climate_risk, conflict_events // 5, disease_outbreaks],
        color_continuous_scale='reds',
        title="TRIPLE-NEXUS RISK SCORE (LIVE)"
    ).update_layout(template='plotly_dark')),

    html.Div(style={
        'fontSize': '2rem',
        'margin': '40px',
        'padding': '20px',
        'background': '#300',
        'border': '2px solid red'
    }, children=[
        "NEXUS WATCH (60–90 days)",
        html.Br(),
        "Turkana-Karamoja cluster: NDVI collapse + displacement + Mpox circulation → 63% conflict surge predicted MAM 2025"
    ]),
    
    html.Footer("Horn of Africa • 2025 • No sleep", style={'position': 'fixed', 'bottom': 0, 'width': '100%'})
])

# Run only for local testing
if __name__ == '__main__':
    app.run_server(server=server, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
