import pandas as pd
import plotly.express as px
import plotly.io as pio
from dash import html, dcc
from pydantic import validate_arguments
import pandas as pd

pio.renderers.default = 'browser'

map_box_token = "pk.eyJ1IjoibWlsYW56bWl0cm92aWMiLCJhIjoiY2w3amlrczY2MHlqZDNxcGJqYmFpZnc0NiJ9.XsJWYsBkbKYloeVtBq2Rlg"
px.set_mapbox_access_token(map_box_token)

gsp_circuits_ = pd.read_csv('etl/transformed_data/gsp_circuits.csv')

concatenated_df_ = pd.read_csv(
    'etl/transformed_data/concatenated_df.csv',
    dtype={
        # 'fieldtime': 'datetime',
    },
    parse_dates=['fieldtime']

)

concatenated_df_.shape
gsp_circuits_.shape

px.line(

)

concatenated_df_.columns

data = (
    concatenated_df_[['fieldtime', '3075746CE13']]
        .groupby(
        by=pd.Grouper(
            key='fieldtime',
            freq='d'
        )).sum().reset_index()
)

concatenated_df_['fieldtime'].dtype

fig = px.line(
    x=data['fieldtime'],
    y=data['3075746CE13'],
    template='simple_white'
)


fig.update_layout(
    margin=dict(t=10, l=10, r=10, b=10),
    yaxis_title='y',
    xaxis_title='x'
)

fig.show()



gsp_circuits_['latitude'].unique()


