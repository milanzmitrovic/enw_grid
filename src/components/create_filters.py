
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


def create_filters(df: pd.DataFrame):

    return dmc.Container([
        dmc.SimpleGrid(
            spacing='lg',
            cols=2,
            breakpoints=[
                {"maxWidth": 980, "cols": 3, "spacing": "md"},
                {"maxWidth": 755, "cols": 2, "spacing": "sm"},
                {"maxWidth": 600, "cols": 1, "spacing": "sm"},
            ],

            style={
                "textAlign": "center",
            },

            children=[

                html.Div([
                    html.H4('Structured Plant Number'),
                    dcc.Dropdown(
                        # Instead of list with dictionaries, you can also put simple list like [1,2,3,4]
                        # But, list with dictionaries gives you more flexibility
                        options=df.columns[2:],
                        value=df.columns[2],
                        id='plant-number'
                    )
                ]),

                html.Div([
                    html.H4('Grouping Frequency (Month, Week, Day)'),
                    dcc.Dropdown(
                        # Instead of list with dictionaries, you can also put simple list like [1,2,3,4]
                        # But, list with dictionaries gives you more flexibility
                        options=[
                            {'label': 'Month', 'value': 'M'},
                            {'label': 'Week', 'value': 'W'},
                            {'label': 'Day', 'value': 'D'},
                        ],
                        value='M',
                        id='month-week-day'
                    ),

                ]),

            ])
    ])

