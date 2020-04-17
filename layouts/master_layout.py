import dash_core_components as dcc
import dash_html_components as html
import dash_table

master = html.Div([ # visuals container   
            html.Div([ # pic column container
                html.H6(id='name-header'),
                html.Img(id='image'), # team or player image
            ], className='two columns'),
            
            html.Div([ # data container
                html.Div([ # graph
                    dcc.Graph(id='data-graph')
                ]),
                html.Div([ # table
                    dash_table.DataTable(id='data-table')
                ])
            ])
        ], className='eight columns')
])