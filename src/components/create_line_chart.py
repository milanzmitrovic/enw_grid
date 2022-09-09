import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio

from src.utils.naming_conventions import id_

pio.renderers.default = 'browser'


def create_line_chart(
        app: Dash,
        df: pd.DataFrame,

):

    # onClick callback
    @callback(
        Output(component_id='plant-number', component_property='value'),
        Input(component_id=id_.scatter_map, component_property='clickData'),
    )
    def f1(
            input_
    ):
        if input_ is not None:
            pt = input_["points"][0]
            hover_text = pt["hovertext"]
            print(hover_text)
        else:
            hover_text = dash.no_update

        return hover_text

    @app.callback(
        Output(component_id='line-chart', component_property='figure'),
        Input(component_id='plant-number', component_property='value'),
        Input(component_id='month-week-day', component_property='value'),
    )
    def f1(
            plant_number,
            grouping_freq
    ):
        data = (df[['fieldtime', plant_number]].groupby(
            by=pd.Grouper(
                key='fieldtime',
                freq=grouping_freq
            )
        ).sum().reset_index())

        fig = px.line(
            x=data['fieldtime'],
            y=data[plant_number],
            template='simple_white'
        )

        fig.update_layout(
            margin=dict(t=0, l=0, r=0, b=0),
            yaxis_title='y',
            xaxis_title='x'
        )

        return fig

    return dmc.Container([
                dcc.Graph(id='line-chart')
    ])

