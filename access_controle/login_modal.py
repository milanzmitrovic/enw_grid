
import random
import time

import dash_mantine_components as dmc
from dash import html, Output, Input, State, callback, dcc, Dash
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash

from access_controle.utils_file import Users


def login_button(app: Dash):

    # Callback for opening modal component
    @app.callback(
        Output("modal_login", "opened"),
        Input("modal-demo-button_login", "n_clicks"),
        Input("modal-submit-button_login", "n_clicks"),
        State("modal_login", "opened"),
        prevent_initial_call=True,
    )
    def modal_demo(nc1, nc2, opened):
        return not opened

    # Callback for logging in
    @app.callback(
        Output('login-status', 'children'),
        Input('login-button', 'n_clicks'),
        State('uname-box', 'value'),
        State('pwd-box', 'value')
    )
    def successful(n_clicks, input1, input2):
        # This step is necessary to prevent initial callback
        if n_clicks is not None and n_clicks > 0:
            print('-------------', n_clicks)

            user = Users.query.filter_by(username=input1).first()
            if user:
                if check_password_hash(user.password, input2):
                    login_user(user)
                    print('User just logged in')
                    print('Login status: ', current_user.is_authenticated)
                    return 'You have just logged in!'
                else:
                    return 'Incorrect username or password'
            else:
                return 'Incorrect username or password 2'

    # Purpose of this callback is to refresh page after logging in!!!
    # Why is it important? --> In order to delete login info from being stored in modal component
    @app.callback(
        Output(component_id='main-url-3', component_property='pathname'),
        Input(component_id='modal-submit-button_login', component_property='n_clicks')
    )
    def f1(
            n_clicks
    ):
        if n_clicks is not None and n_clicks > 0:
            # Why do we have random number?
            # -->
            rnd = random.randint(1, 1000)
            return '/logged-in' + str(rnd)

    return html.Div(
        [

            dmc.Button("Login Modal", id="modal-demo-button_login"),
            dmc.Modal(
                id="modal_login",
                children=[
                    html.H2('''Please log in to continue:''', id='h1'),
                    dcc.Input(
                        placeholder='Enter your username',
                        type='text',
                        id='uname-box'),
                    dcc.Input(
                        placeholder='Enter your password',
                        type='password',
                        id='pwd-box'),
                    html.Button(
                        children='Login',
                        n_clicks=0,
                        type='submit',
                        id='login-button'),
                    html.Br(),
                    html.Br(),

                    html.H3(id='login-status'),

                    dmc.Group(
                        [
                            dmc.Button("Submit", id="modal-submit-button_login")
                        ],
                        position="right",
                    ),
                ],
            ),
        ]
    )

