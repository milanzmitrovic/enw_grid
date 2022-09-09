import json

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio
from pydantic import validate_arguments

from src.utils.naming_conventions import id_

pio.renderers.default = 'browser'


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def create_scatter_map(
        app: Dash,
        df: pd.DataFrame
) -> dmc.Container:

    fig = px.scatter_mapbox(
        lat=df['latitude'],
        lon=df['longitude'],
        hover_name=df['Structured Plant Number'],
        size_max=15,
        zoom=6
    )

    return dmc.Container([
        # Graph
        dcc.Graph(
            id=id_.scatter_map,
            figure=fig
        ),

        dmc.Space(h=0)
    ])





