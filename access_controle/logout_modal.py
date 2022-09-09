
import random
import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback, Dash
from flask_login import logout_user, current_user


def logout_button(app: Dash):

    # Callback for opening modal component
    @app.callback(
        Output("modal_logout", "opened"),
        Input("modal-demo-button_logout", "n_clicks"),
        Input("modal-close-button_logout", "n_clicks"),
        Input("modal-submit-button_logout", "n_clicks"),
        State("modal_logout", "opened"),
        prevent_initial_call=True,
    )
    def modal_demo(nc1, nc2, nc3, opened):
        return not opened

    # Callback for logging out
    @app.callback(
        Output(component_id='logout-status', component_property='children'),
        Input(component_id='logout-button', component_property='n_clicks')
    )
    def logout_user_callback(n_clicks):

        if n_clicks is not None:
            print('Number of clicks:', n_clicks)
            print('User is authenticated:', current_user.is_authenticated)

            if current_user.is_authenticated:
                print(321)
                logout_user()
                return 'You have just logged out!'
            else:
                return 'You are not logged in. Please log in first!'

    # I can't remember what is this used for
    # But, I thing it's purpose is to prevent going backward in browser???
    # --> Purpose of this callback is to refresh page after logging out!!!
    @app.callback(
        Output(component_id='main-url-2', component_property='pathname'),

        Input(component_id='logout-button', component_property='n_clicks'),
        State(component_id='main-url', component_property='pathname')
    )
    def f1(
            n_clicks,
            main_url
    ):
        if n_clicks is not None and n_clicks > 0:
            return '/logout-url' + str(random.randint(1, 10000))

    return html.Div(
            [
                dmc.Button("Logout Modal", id="modal-demo-button_logout"),
                dmc.Modal(
                    title="Logout Modal",
                    id="modal_logout",
                    children=[
                        dmc.Text("I am in a modal component."),
                        dmc.Space(h=20),

                        dmc.Button('Click here to logout!', id='logout-button'),
                        html.H3(id='logout-status'),


                        dmc.Group(
                            [
                                dmc.Button("Submit", id="modal-submit-button_logout"),
                                dmc.Button(
                                    "Close",
                                    color="red",
                                    variant="outline",
                                    id="modal-close-button_logout",
                                ),
                            ],
                            position="right",
                        ),
                    ],
                ),
            ]
        )


