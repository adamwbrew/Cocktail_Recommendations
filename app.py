import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

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
                            html.Img(id='logo', src="assets/Logo_DARKLY.png", height="150px"),
                            width="auto",
                        ),
                        dbc.Col(
                            dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink(page['name'].title(), href=page['path'],
                                                             style={'fontSize': '20px'}))
                                    for page in dash.page_registry.values()
                                ],
                                navbar=True,
                            ),
                            width="auto"
                        ),
                    ],
                    justify="center",  # Add this property to center the image
                    align="center",
                ),
                # Add fluid class to the container to make it full-width on small devices
            ],
            fluid=True,  # Add this property to make the container full-width on small devices
        ),
        color="dark",
        dark=True,
        className="mb-5",
        sticky="top"
    ),
    dash.page_container
])

@app.callback(Output('logo', 'height'),
              [Input('url', 'pathname')])
def update_logo_height(pathname):
    if 'mobile' in pathname:
        return '100px'
    else:
        return '150px'

if __name__ == '__main__':
    app.run_server(debug=True)