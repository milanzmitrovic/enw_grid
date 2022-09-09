

import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback, dcc, Dash
from flask_login import current_user
from werkzeug.security import generate_password_hash

from access_controle.utils_file import Users_tbl, engine


def create_user_button(app: Dash):

    # Callback for opening modal component
    @app.callback(
        Output("modal_create_user", "opened"),
        Input("modal-demo-button_create_user", "n_clicks"),
        Input("modal-close-button_create_user", "n_clicks"),
        Input("modal-submit-button_create_user", "n_clicks"),
        State("modal_create_user", "opened"),
        prevent_initial_call=True,
    )
    def modal_demo(nc1, nc2, nc3, opened):
        print(current_user.is_authenticated)
        return not opened

    # Callback for creating new user
    @app.callback(
        Output('create-user-status', "children"),
        Input('submit-val', 'n_clicks'),
        State('username', 'value'),
        State('password', 'value'),
        State('email', 'value')
    )
    def insert_users(n_clicks, un, pw, em):
        # hashed_password = generate_password_hash(pw, method='sha256')
        if un is not None and pw is not None and em is not None:
            hashed_password = generate_password_hash(pw, method='sha256')
            ins = Users_tbl.insert().values(username=un, password=hashed_password, email=em, )
            conn = engine.connect()
            conn.execute(ins)
            conn.close()
            return 'User successfully created!'
        else:
            return 'User already have an account!'

    return html.Div(
            [
                dmc.Button("Create User Modal", id="modal-demo-button_create_user"),
                dmc.Modal(
                    title="Login Modal",
                    id="modal_create_user",
                    children=[
                        dmc.Text("I am in a modal component."),
                        dmc.Space(h=20),

                        html.Div(
                            [
                                html.H1('Create User Account'),
                                dcc.Input(
                                    id="username",
                                    type="text",
                                    placeholder="user name",
                                    maxLength=15
                                ),
                                dcc.Input(
                                    id="password",
                                    type="password",
                                    placeholder="password"
                                ),
                                dcc.Input(
                                    id="email",
                                    type="email",
                                    placeholder="email",
                                    maxLength=50
                                ),
                                html.Button(
                                    'Create User',
                                    id='submit-val',
                                    n_clicks=0
                                ),
                                html.Div(
                                    id='create-user-div'),
                                  html.Br(),
                            ]
                        ),

                        html.H3(id='create-user-status'),


                        dmc.Group(
                            [
                                dmc.Button("Submit", id="modal-submit-button_create_user"),
                                dmc.Button(
                                    "Close",
                                    color="red",
                                    variant="outline",
                                    id="modal-close-button_create_user",
                                ),
                            ],
                            position="right",
                        ),
                    ],
                ),
            ]
        )




