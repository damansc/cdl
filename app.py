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

app.title = 'CDL Stats Lab'
app.layout = html.Div([
    
    html.Div([
        
        html.Div([
            html.H1('CDL Stats Lab')    
        ]),
        
        dcc.Store(id='data-store'),
    
        html.Div([ # input container
                  
            html.Div([ # radio inputs
                      
                dcc.RadioItems(id='mode-select', 
                               options = [
                                   {'label': 'SnD', 'value': 'snd'},
                                   {'label': 'HP', 'value': 'hp'},
                                   {'label': 'Dom', 'value': 'dom'}
                               ],
                               value='',
                               labelStyle={'display': 'inline-block'}),
                dcc.RadioItems(id='view-select',
                               options = [
                                   {'label': 'Players', 'value': 'players'},
                                   {'label': 'Teams', 'value': 'teams'}
                               ],
                               value='',
                               labelStyle={'display': 'inline-block'})
            ]),
         
            html.Div([ # user inputs
                dcc.Dropdown(id='target-drop'),
                dcc.Dropdown(id='stat-drop')
            ]),
            
            html.Div([
                html.Img(id='target-image', style={'margin-top': 50, 'padding': 10, 'height': '100%', 'width': '100%', "border":"2px black solid"})
            ]),
        ], className='two columns'),
        
        html.Div([ # data container
            html.Div([
                dcc.Graph(id='compare-graph')
            ]),
            html.Div([
                dash_table.DataTable(id='dash-table',
                                     virtualization=True,
                                     )
            ])
        ], className='eight columns', style={"border":"2px black solid"}),
        
    ])
])

# reads in the chosen mode data
@app.callback(
    Output('data-store', 'data'),
    [Input('mode-select', 'value')]
)
def read_mode_data(mode):
    if mode == 'snd':
        data = pd.read_excel('data/mode_db_snd_data.xlsx',
                             sheet_name='snd')
    elif mode == 'hp':
        data = pd.read_excel('data/mode_db_hp_data.xlsx',
                             sheet_name='hp')
    elif mode == 'dom':
        data = pd.read_excel('data/mode_db_dom_data.xlsx',
                             sheet_name='dom')
    return data.to_json()

# updates the dropdown value attributes
@app.callback(
    [Output('target-drop', 'options'),
    Output('stat-drop', 'options')],
    [Input('data-store', 'data'),
     Input('view-select', 'value'),
     Input('mode-select', 'value')]
)
def update_dropdown(data, view, mode):
    raw_data = pd.read_json(data)
    if mode == 'hp':
        stats = [{'label':i, 'value': i} for i in raw_data.columns[12:-1]]
    elif mode == 'snd':
        stats = [{'label':i, 'value': i} for i in raw_data.columns[10:-1]]
    elif mode == 'dom':
        stats = [{'label':i, 'value': i} for i in raw_data.columns[12:-4]]
    else:
        pass
    if view == 'players':
        targets = [{'label': i, 'value':i} for i in raw_data.Player.unique()]
    if view == 'teams':
        targets = [{'label': i, 'value':i} for i in raw_data.Team.unique()]
    return targets, stats

# pic callback
@app.callback(
    Output('target-image', 'src'),
    [Input('target-drop', 'value')]
)
def updated_picture(target):
    targ = target
    return f'assets/{targ}.png'

# figure callback
@app.callback(
    Output('compare-graph', 'figure'),
    [Input('target-drop', 'value'),
     Input('stat-drop', 'value'),
     Input('data-store', 'data')]
)
def update_graph(target, stat, data):
    data = pd.read_json(data)
    if target in data.Player.unique():
        focus = data[(data.Player == target)]
        target_data = focus.groupby('Date')[stat].mean().reset_index()
        target_data['type'] = 'selected'
        pop_data = data.groupby('Date')[stat].mean().reset_index()
        pop_data['type'] = 'Field'
    elif target in data.Team.unique():
        focus = data[(data.Team == target)]
        target_data = focus.groupby('Date')[stat].mean().reset_index()
        target_data['type'] = 'selected'
        pop_data = data.groupby('Date')[stat].mean().reset_index()
        pop_data['type'] = 'Field'
    output = pd.concat([target_data, pop_data], axis=0)
    return px.scatter(output, x='Date', y=stat, color='type')

@app.callback(
    Output('dash-table', 'columns'),
    [Input('data-store', 'data')]
)
def update_table_columns(data):
    return [{'name': i, 'id': i} for i in pd.read_json(data).columns]

@app.callback(
    Output('dash-table', 'data'),
    [Input('target-drop', 'value'),
     Input('stat-drop', 'value'),
     Input('data-store', 'data')]
)
def update_table(target, stat, data):
    df = pd.read_json(data)
    if target in df.Player.unique():
        focus = df[(df.Player == target)]
        export = focus.to_dict('records')
    elif target in df.Team.unique():
        focus = df[(df.Team == target)]
        export = focus.to_dict('records')
    return export

    
if __name__ == "__main__":
    app.run_server(debug=True)