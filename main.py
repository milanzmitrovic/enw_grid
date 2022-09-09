from dash import html
from access_controle.init_access_controle import create_access_controle_components
from src.components.create_filters import create_filters
from src.components.create_header_component import create_header_component
from src.components.create_line_chart import create_line_chart
from src.components.create_scatter_map import create_scatter_map
import pandas as pd
from access_controle.utils_file import dash_app
import plotly.express as px
import dash_mantine_components as dmc

from src.utils.tabs_main_logic import create_tab_components

map_box_token = "pk.eyJ1IjoibWlsYW56bWl0cm92aWMiLCJhIjoiY2w3amlrczY2MHlqZDNxcGJqYmFpZnc0NiJ9.XsJWYsBkbKYloeVtBq2Rlg"

px.set_mapbox_access_token(map_box_token)

gsp_circuits_ = pd.read_csv(
    'etl/transformed_data/gsp_circuits.csv'
)

concatenated_df_ = pd.read_csv(
    'etl/transformed_data/concatenated_df.csv',
    parse_dates=['fieldtime']
)

dash_app.layout = html.Div([

    create_header_component(app=dash_app),

    create_tab_components(app_=dash_app),

    create_filters(df=concatenated_df_),

    create_access_controle_components(app=dash_app),

    dmc.Space(h=40),

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

                create_scatter_map(
                    app=dash_app,
                    df=gsp_circuits_
                ),

            ]),

            html.Div([
                create_line_chart(
                    app=dash_app,
                    df=concatenated_df_
                )

            ]),

        ])

])

# validate_layout(app_=app)


if __name__ == '__main__':
    dash_app.run_server(debug=True)
