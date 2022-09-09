
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px


def create_tab_components(
        app_: Dash
):
    # Callback for switching tabs
    @app_.callback(
        Output(component_id='tabs-content-example-graph', component_property='children'),
        Input(component_id='tabs-example-graph', component_property='value')
    )
    def render_content(tab):
        if tab == 'tab-1-example-graph':
            # Return should contain desired output
            return html.Div([
                html.H3('Tab content 1')
            ])
        elif tab == 'tab-2-example-graph':
            # Return should contain desired output
            return html.Div([
                html.H3('Tab content 2')
            ])

    return html.Div([

        dmc.Space(h=40),
        dcc.Tabs(
            id="tabs-example-graph",
            value='tab-1-example-graph',
            children=[
                dcc.Tab(label='Tab One', value='tab-1-example-graph'),
                dcc.Tab(label='Tab Two', value='tab-2-example-graph'),
            ]
        ),

        # HTML component to be updated based on tab selected
        html.Div(id='tabs-content-example-graph')
    ])


