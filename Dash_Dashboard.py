import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import plotly.graph_objs as go
from draw_rink import draw_rink
from Plotly_Rink import rink_shapes
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

conts_DF = pd.read_csv('Shot_Database_2015-2019.csv')

x = conts_DF['X-Location']
y = conts_DF['Y-Location']

app = dash.Dash()
server = app.server
"""
def update_chart():
    
    x = [0,25,26]
    y = [0,26,28]
    kde_plot = sns.scatterplot(x,y)
    ax = kde_plot.axes
    draw_rink(ax)
    
    #Setting the size of the figure
    #sns.set(rc={'figure.figsize':(8.0,10.0)})
    # Change the style of the axes/background
    sns.set_style("white")
    # Remove the axes ticks and spines
    ax.set_yticks([])
    ax.set_xticks([])
    sns.despine(left=True,bottom=True)
    ax.set_xlabel("")
    ax.set_ylabel("")
    # Set alpha of the kdeplot to see background
    #ax.collections[0].set_alpha(0.001)
    plt.xlim(-50,50)
    plt.ylim(0,100)
    return ax
"""
layout = go.Layout(
        title='2015-2019',
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
data = [go.Histogram2dContour(x = y, y = x,
                              colorscale = [[0, 'rgb(255,255,255)'],[1, 'rgb(0,10,255)']],
                              opacity = 0.7,
                              reversescale=False,
                              ncontours=10,
                              histfunc = 'avg'
                              )]               
 
                
fig = go.Figure(layout = layout, data=data)

app.layout = html.Div(children=[html.H1('NHL Shot Dashboard'),
                                dcc.Graph(id='NHL_Rink',figure = fig)
                                ])

if __name__ == '__main__':
    app.run_server(debug=True,host='localhost')

    