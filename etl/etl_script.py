

from pyproj import Proj, transform
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


v84 = Proj(proj="latlong",towgs84="0,0,0",ellps="WGS84")
v36 = Proj(
    proj="latlong",
    k=0.9996012717,
    ellps="airy",
    towgs84="446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894"
)

vgrid = Proj(init="world:bng")


def ENtoLL84(easting, northing):
    """Returns (longitude, latitude) tuple
    """
    vlon36, vlat36 = vgrid(easting, northing, inverse=True)
    return transform(v36, v84, vlon36, vlat36)


def LL84toEN(longitude, latitude):
    """Returns (easting, northing) tuple
    """
    vlon36, vlat36 = transform(v84, v36, longitude, latitude)
    return vgrid(vlon36, vlat36)


gsp_voltage = pd.read_excel(
    'etl/raw_data/gsp_boundary_flow.xlsx',
    engine='openpyxl',
    sheet_name='GSP_Voltage'
)
gsp_voltage['sheet_name'] = 'gsp_voltage'


gsp_circuits = pd.read_excel(
    'etl/raw_data/gsp_boundary_flow.xlsx',
    engine='openpyxl',
    sheet_name='GSP Circuits'
)
gsp_circuits['sheet_name'] = 'gsp_circuits'


gsp_mvAr = pd.read_excel(
    'etl/raw_data/gsp_boundary_flow.xlsx',
    engine='openpyxl',
    sheet_name='GSP_MVAr'
)
gsp_mvAr['sheet_name'] = 'gsp_mvar'


gsp_mw = pd.read_excel(
    'etl/raw_data/gsp_boundary_flow.xlsx',
    engine='openpyxl',
    sheet_name='GSP_MW'
)
gsp_mw['sheet_name'] = 'gsp_mw'


gsp_current = pd.read_excel(
    'etl/raw_data/gsp_boundary_flow.xlsx',
    engine='openpyxl',
    sheet_name='GSP_Current'
)
gsp_current['sheet_name'] = 'gsp_current'


concatenated_df = pd.concat([
    gsp_voltage,
    gsp_mvAr,
    gsp_mw,
    gsp_current
])


concatenated_df.to_csv('etl/transformed_data/concatenated_df.csv')
concatenated_df_ = pd.read_csv('etl/transformed_data/concatenated_df.csv')


est = gsp_circuits['Easting']
nor = gsp_circuits['Northing']


ENtoLL84(easting=est, northing=nor)
longitude = ENtoLL84(easting=est, northing=nor)[0]
lattitude = ENtoLL84(easting=est, northing=nor)[1]


gsp_circuits['latitude'] = lattitude
gsp_circuits['longitude'] = longitude


gsp_circuits.to_csv('etl/transformed_data/gsp_circuits.csv')
gsp_circuits_ = pd.read_csv('etl/transformed_data/gsp_circuits.csv')


