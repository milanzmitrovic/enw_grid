
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
from flask_login import current_user


def login_status(app: Dash):

    @app.callback(
        Output(component_id='login-status_', component_property='children'),
        Input(component_id='login-check', component_property='n_clicks')
    )
    def main_page_view(n_clicks):
        if n_clicks is not None and n_clicks > 0:
            return f'Current user is logged in - {current_user.is_authenticated}'

    return html.Div([
        html.Button('Check if user is logged in!', id='login-check'),
        html.H1(id='login-status_')

    ])
