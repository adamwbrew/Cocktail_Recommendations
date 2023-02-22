import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.DARKLY, FA])
server = app.server


# the styles for the main content position it to the right of the sidebar and
# add some padding.



# app.layout = dbc.Container([
#     dbc.NavbarSimple([
#         dbc.NavItem(dbc.NavLink(page['name'].title(), href=page['path']))
#         for page in dash.page_registry.values()
#     ], 
#     dark = True,
#     color = "dark",
#     expand = "lg",
#     sticky = "top"
#     ),
#     dash.page_container
# ])

app.layout = dbc.Container([
    dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src="assets/logo_DARKLY.png", height="150px", id="logo"),
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
            ],
            fluid=True,  # Add this property to make the container full-width on small devices
        ),
        color="dark",
        dark=True,
        className="mb-5",
        sticky="top",
    ),
    dash.page_container
])

# Add this CSS code to set the height of the logo to 100px on small devices
app.clientside_callback(
    """
    function(width) {
        if (width <= 576) {
            document.getElementById("logo").height = "100px";
        } else {
            document.getElementById("logo").height = "150px";
        }
    }
    """,
    Output("logo", "children"),
    [Input("window-width", "innerWidth")]
)

# Add this hidden div to get the current window width
app.layout.append(dbc.Input(id="window-width", type="hidden"))


if __name__ == '__main__':
    app.run_server(debug=True)

