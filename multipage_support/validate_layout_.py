
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px


def validate_layout(
        app_: Dash
):

    # "complete" layout
    # Here should come list of all html elements used within app
    app_.validation_layout = html.Div([

    ])

    return ''




