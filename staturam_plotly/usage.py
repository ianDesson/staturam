import staturam_plotly
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='arm-left-down',
        figure={
            'data': [
                go.Scatter(
                    x=['Leaning-angle', 'Shoulder-elbow-wrist', 'Hip-shoulder-Elbow'],
                    y=[4.75, 110, 68],
                    error_y=dict(
                        type='data',
                        array=[5, 5, 5],
                        visible=True
                    ),
                    name='Professional Data'
                ),
                go.Scatter(
                    x=['Leaning-angle', 'Shoulder-elbow-wrist', 'Hip-shoulder-Elbow'],
                    y=[3, 155, 1.75],
                    name="Your Data"
                )
            ],
            'layout': {
                'title': 'Bicep Curl Down - Right Side',
                'yaxis': {
                    'title': 'Angles in Degrees'
                }
            }
        }
    ),
    dcc.Graph(
        id='arm-left-middle',
        figure={
            'data': [
                go.Scatter(
                    x=['Leaning-angle', 'Shoulder-elbow-wrist', 'Hip-shoulder-Elbow'],
                    y=[6.01, 103.97, 82.7],
                    error_y=dict(
                        type='data',
                        array=[5, 5, 5],
                        visible=True
                    ),
                    name='Professional Data'
                ),
                go.Scatter(
                    x=['Leaning-angle', 'Shoulder-elbow-wrist', 'Hip-shoulder-Elbow'],
                    y=[4.5, 70, 45],
                    name='Your Data'
                )
            ],
            'layout': {
                'title': 'Bicep Curl Middle - Left Side',
                'yaxis': {
                    'title': 'Angles in Degrees'
                }
            }
        }
    ),
    dcc.Graph(
        id='arm-left-up',
        figure={
            'data': [
                go.Scatter(
                    x=['Leaning-angle', 'Shoulder-elbow-wrist', 'Hip-shoulder-Elbow'],
                    y=[3.37, 71.9, 42.83],
                    error_y=dict(
                        type='data',
                        array=[5, 5, 5],
                        visible=True
                    ),
                    name='Professional Data'
                ),
                go.Scatter(
                    x=['Leaning-angle', 'Shoulder-elbow-wrist', 'Hip-shoulder-Elbow'],
                    y=[16.64, 38, 11],
                    name='Your Data'
                )
            ],
            'layout': {
                'title': 'Bicep Curl Up - Left Side',
                'yaxis': {
                    'title': 'Angles in Degrees'
                }
            }
        }
    ),
])


def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
