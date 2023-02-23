import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.Div(children=[
        dcc.Markdown(
            '''
            Welcome to our cocktail information and recommendation app!

            Are you tired of ordering the same old drink every time you go out? Do you want to try new and exciting cocktail recipes that match your taste preferences? Look no further! Our app is here to help you discover and enjoy delicious cocktails that are perfect for you.

            Our app features three powerful tools that can help you find the perfect cocktail recipe:

            * #### **Cocktail Search**:
            The Cocktail Search page is a powerful tool that allows you to search through our comprehensive database of cocktail recipes. You'll find information on the main liquor used, a list of ingredients, instructions on how to make the cocktail, preferred glassware, garnishes, and the source of the recipe, if known.

            * #### **Cocktail Based Recommendations**:
            The Cocktail Based Recommendations page lets you easily find new cocktail recommendations based on your existing preferences. Simply input one or more cocktails that you already enjoy, and our app will generate three personalized cocktail recommendations tailored to your tastes.

            * #### **Ingredient Based Recommendations**:
            The Ingredient Based Recommendations page is a great way to discover new cocktails based on the specific ingredients you're in the mood for. Simply enter one or more ingredients that you'd like to include in your cocktail, and our app will provide you with three personalized cocktail recommendations that match your preferences.

            We're excited to help you discover new and exciting cocktail recipes that you'll love. Our app is easy to use and provides detailed information on each recipe, so you can create your perfect drink at home or order confidently at the bar.

            Please note that due to the lack of proper instructions for some cocktails, the instructions to create certain cocktails may not be properly constructed. However, we're constantly working to improve our database and update our instructions.

            If you have any questions or feedback, please don't hesitate to contact us. We're always happy to hear from our users. And if you're interested in learning about how our app was made, check out our GitHub repository by scanning or clicking the QR code below.

            Cheers, and happy cocktail-making!
            '''
        ),
        html.Br(),
        html.Div(
            [
                html.A(
                    html.Img(src="assets/QR_Git.png", height="200px"),
                    href="https://github.com/adamwbrew/Cocktail_Recommendations",
                )
            ],
            style={'textAlign': 'center'}
        )
    ], style={'fontSize': '20px'})
])