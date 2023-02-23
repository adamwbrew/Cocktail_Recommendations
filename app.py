import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
from user_agents import parse
from flask import request

FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY, FA],
                meta_tags=[{'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])
server = app.server

app.layout = dbc.Container(className="mt-4 mb-4", children=[
    dcc.Location(id='url', refresh=False),
    dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(id='logo'),
                            width="auto",
                        ),
                        dbc.Col(
                            dbc.Nav(
                                dbc.NavbarToggler( id='navbar-toggler'),
                                className="ml-auto",
                            ),
                            width="auto"
                        ),
                    ],
                    justify="center",  # Add this property to center the image
                    align="center",
                ),
                dbc.Collapse(dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink(page['name'].title(), href=page['path'],
                                                             style={'fontSize': '20px', 'px': '10px', 'py': '8px'}))
                                    for page in dash.page_registry.values()
                                ],
                                navbar=True,
                                className="d-flex justify-content-between flex-grow-1"
                            ), id="navbar-collapse", navbar=True),
                # Add fluid class to the container to make it full-width on small devices
            ],
            fluid=True,  # Add this property to make the container full-width on small devices
        ),
        color="dark",
        dark=True,
        className="mb-5",
        sticky="top",
        expand="lg" # Add this attribute to make the navbar responsive
    ),
    dash.page_container
])

@app.callback(Output('logo', 'children'),
              [Input('url', 'pathname')])
def update_logo_height(pathname):
    user_agent = parse(request.headers['User-Agent'])
    if user_agent.is_mobile:
        return html.Img(src="assets/Logo_DARKLY.png", height="100px")
    else:
        return html.Img(src="assets/Logo_DARKLY.png", height="150px")

@app.callback(Output('navbar-collapse', 'is_open'),
              [Input('navbar-toggler', 'n_clicks')],
              [State('navbar-collapse', 'is_open')])
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks is not None:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)