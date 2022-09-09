import dash_mantine_components as dmc
from dash import html, dcc, Dash
from dash_iconify import DashIconify

from access_controle.login_modal import login_button
from access_controle.logout_modal import logout_button


def create_home_link(label):
    return dmc.Text(
        label,
        size="xl",
        color="gray",
    )


def create_header_component(app: Dash):
    return dmc.Header(
        height=70,
        # fixed=True, # uncomment this line if you are using this example in your app
        p="md",
        children=[
            dmc.Container(
                fluid=True,
                children=dmc.Group(
                    position="apart",
                    align="flex-start",
                    children=[
                        dmc.Center(
                            dcc.Link(
                                [
                                    dmc.MediaQuery(
                                        create_home_link("ENW Demo Data App"),
                                        smallerThan="sm",
                                        styles={"display": "none"},
                                    ),
                                    dmc.MediaQuery(
                                        create_home_link("DMC"),
                                        largerThan="sm",
                                        styles={"display": "none"},
                                    ),
                                ],
                                href="/",
                                style={"paddingTop": 5, "textDecoration": "none"},
                            ),
                        ),
                        dmc.Group(
                            position="right",
                            align="center",
                            spacing="xl",
                            children=[


                                login_button(app=app),
                                logout_button(app=app),


                            ],
                        ),
                    ],
                ),
            )
        ],
    )
