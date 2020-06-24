# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from Plotly_Rink import rink_shapes

app = dash.Dash(__name__)
server = app.server


#Import the data
data_Shots = pd.read_csv('Shot_database_2015-2019_Processed.csv')

app.layout = html.Div([
    
    html.H1("NHL Shot Dashboard"),
    
    dcc.Dropdown(id = "select_year",
                     options=[
                         {"label": "2015", "value" : 2015},
                         {"label": "2016", "value" : 2016},
                         {"label": "2017", "value" : 2017},
                         {"label": "2018", "value" : 2018},
                         {"label": "2019", "value" : 2019}],
                     multi=False,
                     value = 2015,
                     style={'width': "40%"}
                     ),
    
    dcc.Dropdown(id = "select_team",
                     options=[
                         {"label": "All Teams", "value" : 'All'},
                         {"label": "Anaheim Ducks", "value" : 'ANA'},
                         {"label": "Arizona Coyotes", "value" : 'ARI'},
                         {"label": "Boston Bruins", "value" : 'BOS'},
                         {"label": "Buffalo Sabres", "value" : 'BUF'},
                         {"label": "Carolina Hurricanes", "value" : 'CAR'},
                         {"label": "Calgary Flames", "value" : 'CGY'},
                         {"label": "Chicago Blackhawks", "value" : 'CHI'},
                         {"label": "Columbus Blue Jackets", "value" : 'CBJ'},
                         {"label": "Colorado Avalanche", "value" : 'COL'},
                         {"label": "Dallas Stars", "value" : 'DAL'},
                         {"label": "Detroit Red Wings", "value" : 'DET'},
                         {"label": "Edmonton Oilers", "value" : 'EDM'},
                         {"label": "Florida Panthers", "value" : 'FLA'},
                         {"label": "Los Angeles Kings", "value" : 'LAK'},
                         {"label": "Minnesota Wild", "value" : 'MIN'},
                         {"label": "Montreal Canadiens", "value" : 'MTL'},
                         {"label": "Nashville Predators", "value" : 'NSH'},
                         {"label": "New Jersey Devils", "value" : 'NJD'},
                         {"label": "New York Islanders", "value" : 'NYI'},
                         {"label": "New York Rangers", "value" : 'NYR'},
                         {"label": "Ottawa Senators", "value" : 'OTT'},
                         {"label": "Philadelphia Flyers", "value" : 'PHI'},
                         {"label": "Pittsburgh Penguins", "value" : 'PIT'},
                         {"label": "San Jose Sharks", "value" : 'SJS'},
                         {"label": "St. Louis Blues", "value" : 'STL'},
                         {"label": "Tampa Bay Lightning", "value" : 'TBL'},
                         {"label": "Toronto Maple Leafs", "value" : 'TOR'},
                         {"label": "Vancouver Canucks", "value" : 'VAN'},
                         {"label": "Vegas Golden Knights", "value" : 'VGK'},
                         {"label": "Winnipeg Jets", "value" : 'WPG'},
                         {"label": "Washington Capitals", "value" : 'WSH'}],
                         
                         multi = False,
                         value = 'All',
                         style={'width':"40%"},
                         ),

    
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    dcc.Graph(id='shot_map', figure = {})
    
    ])

@app.callback(
    [Output(component_id='output_container',component_property='children'),
     Output(component_id='shot_map',component_property = 'figure')],
    [Input(component_id='select_year',component_property = 'value'),
     Input(component_id='select_team',component_property='value')])


def update_graph(option_selected,team_selected):
    
    print(option_selected)
    
    container = []
    
    layout = go.Layout(
        title=option_selected,
        
        hovermode='closest',
        shapes=rink_shapes(),
        yaxis=dict(
            range=[0, 100],
            scaleanchor="x",
            scaleratio=1,
            ticks='',
            showticklabels=True,
            zeroline=False,
            showgrid=False),
        xaxis=dict(
            range=[-50, 50],
            ticks='',
            showticklabels=True,
            zeroline=False,
            showgrid=False),
        height=700,
        width=700,
    )
    
    dff = data_Shots.copy()
    dff = dff[dff['Year'] == option_selected]
    
    if team_selected == 'All':
        pass
    else:
        dff = dff[dff['Team'] == team_selected]
    
    x = dff['X-Location']
    y = dff['Y-Location']
    
    data = [go.Histogram2dContour(x = y, y = x,
                              colorscale = [[0, 'rgb(255,255,255)'],[1, 'rgb(0,10,255)']],
                              opacity = 0.7,
                              reversescale=False,
                              ncontours=10,
                              histfunc = 'avg'
                              )]  
    
    
    
    fig = go.Figure(layout = layout, data=data)
    
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)


































