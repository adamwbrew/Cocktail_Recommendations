import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/About')

layout = html.Div(children=[
    html.Div(children=[
        dcc.Markdown(
            '''
            Welcome to our cocktail information and recommendation app!

            Do you want to explore new cocktail recipes that perfectly match your taste preferences? Our app is here to help! With three powerful tools, you can discover and enjoy delicious cocktails that are perfect for you.

            Our app features three powerful tools that can help you find the perfect cocktail recipe:

            * #### **Cocktail Search**:
            Our Cocktail Search page is a comprehensive tool that enables you to search through our extensive database of cocktail recipes. You will find information on the main liquor used, a list of ingredients, instructions on how to make the cocktail, preferred glassware, garnishes, and the recipe's source, if available.

            * #### **Cocktail Based Recommendations**:
            Our Cocktail Based Recommendations page provides you with new cocktail recommendations based on your existing preferences. Simply input one or more cocktails that you already enjoy, and our app will generate three personalized cocktail recommendations tailored to your tastes.

            * #### **Ingredient Based Recommendations**:
            The Ingredient Based Recommendations page allows you to discover new cocktails based on specific ingredients you're in the mood for. Simply enter one or more ingredients you'd like to include in your cocktail, and our app will provide you with three personalized cocktail recommendations that match your preferences.

            We want to help you discover exciting cocktail recipes you'll love. Our app is easy to use and provides detailed information on each recipe, so you can create your perfect drink at home or order confidently at the bar.

            Please note that some cocktails may not have proper instructions due to a lack of available information. We're continuously working to enhance our database and update our instructions.

            If you have any questions or feedback, please don't hesitate to contact us. We're always thrilled to hear from our users. And if you're interested in learning how our app was made, check out our GitHub repository by scanning or clicking the QR code below.

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