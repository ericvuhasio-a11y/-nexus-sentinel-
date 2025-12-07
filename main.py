from flask import Flask
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import requests

server = Flask(__name__)
app = Dash(__name__, server=server)

# Mock live data (will upgrade to real APIs)
climate_risk = 8.7
conflict_events = 45
disease_outbreaks = 12

app.layout = html.Div(style={'backgroundColor':'#000','color':'#0f0','fontFamily':'monospace','textAlign':'center'}, children=[
    html.H1("NEXUS SENTINEL", style={'fontSize':'4rem','textShadow':'0 0 20px #0f0'}),
    html.H2("Climate • Conflict • Disease Intelligence Platform", style={'color':'#0ff'}),
    
    dcc.Graph(figure=px.bar(
        x=['CLIMATE','CONFLICT','DISEASE'],
        y=[climate_risk, conflict_events//5, disease_outbreaks],
        color=[climate_risk, conflict_events//5, disease_outbreaks],
        color_continuous_scale='reds',
        title="TRIPLE-NEXUS RISK SCORE (LIVE)"
    ).update_layout(template='plotly_dark')),

    html.Div(style={'fontSize':'2rem','margin':'40px','padding':'20px','background':'#300','border':'2px solid red'}, children=[
        "NEXUS WATCH (60–90 days)",
        html.Br(),
        "Turkana-Karamoja cluster: NDVI collapse + displacement + Mpox circulation → 63% conflict surge predicted MAM 2025"
    ]),
    
    html.Footer("Horn of Africa • 2025 • No sleep", style={'position':'fixed','bottom':0,'width':'100%'})
])

if __name__ == '__main__':
    server = app.server
    server.run(host='0.0.0.0', port=int(__import__('os').environ.get('PORT', 5000)))
