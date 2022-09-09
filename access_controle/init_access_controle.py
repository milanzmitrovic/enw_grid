import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio

from access_controle.create_user_modal import create_user_button
from access_controle.login_modal import login_button
from access_controle.login_status import login_status
from access_controle.logout_modal import logout_button

pio.renderers.default = 'browser'


def create_access_controle_components(app: Dash):
    return dmc.Container([

        dcc.Location(id='main-url', refresh=False),

        # ------------------------- #
        # This component is used for refreshing page after logging out
        dcc.Location(id='main-url-2', refresh=True),

        # ------------------------- #

        # This component is used for refreshing page after logging in
        dcc.Location(id='main-url-3', refresh=True),

        html.Div(id='main-url2-div'),

        html.Div(id='main-content'),

        # login_button(app=app),


        # logout_button(app=app),



        # create_user_button(app=app),



        # ------
        # ------
        # login_status(app=app),

    ])


