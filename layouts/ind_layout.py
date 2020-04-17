individual = html.Div([

    html.Div([ # input container
              
        html.Div([
            dcc.RadioItems(id='view-radio',
                           options=[
                               {'label': i, 'value': i} for i in ['Players',
                                                                  'Teams']
                           ],
                           value='Players'
            )
        ]),
        html.Div([
            dcc.Dropdown(id='drop-input')
        ]),
    ], className='two columns'),
    
    html.Div([ # visuals container
              
        html.Div([ # pic column container
            html.H6(id='name-header')
            dcc.Image(), # team or player image
         ], className='two columns'),
        
        html.Div([ # data container
            html.Div([ # graph
                dcc.Graph()
            ]),
            html.Div([ # table
                dash_table.datatable()
            ])
        ])
    ], className='eight columns')
])

@app.callback(
    Output('drop-input', 'options'),
    [Input('view-radio', 'value')]
)
def update_dropdown(selection):
    if selection == 'Players':
        return [{'label': i, 'value':i} for i in active_players]
    if selection == 'Teams':
        return [{'label': i, 'value':i} for i in active_teams]