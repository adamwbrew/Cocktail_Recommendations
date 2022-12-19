import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is an application made to help give information on cocktails and use recommendation services to help find cocktails someone might like based on ingredients or already known cocktail preferences. 
    '''),

])