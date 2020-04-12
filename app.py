import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pickle
import requests
from datetime import datetime as dt
import dash_table
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets=external_stylesheets
)

server = app.server

app.title = 'CDL Stats'
app.layout = html.Div([
    
    html.Div([
        
        html.Div([
            html.H1('CDL Stats Lab')
        ])
        
        ]) 

])