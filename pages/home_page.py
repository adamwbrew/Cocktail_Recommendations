import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/')

layout = html.Div(children=[

    html.Div(children=[
                
        dcc.Markdown(
             '''
            Welcome to our cocktail information and recommendation app! Are you tired of ordering the same old drink every time you go out? Do you want to try new and exciting cocktail recipes that match your taste preferences? Look no further! Our app is here to help you discover and enjoy delicious cocktails that are perfect for you.

            Our app features three powerful tools that can help you find the perfect cocktail recipe: 
            

            * #### **Cocktail Search**:
            The Cocktail Search page is a powerful tool that allows you to search through our comprehensive database of cocktail recipes. You'll find information on the main liquor used, a list of ingredients, instructions on how to make the cocktail, preferred glassware, garnishes, and the source of the recipe, if known.

            
            * #### **Cocktail Based Recommendations**:
            The Cocktail Based Recommendations page lets you easily find new cocktail recommendations based on your existing preferences. Simply input one or more cocktails that you already enjoy, and our app will generate three personalized cocktail recommendations tailored to your tastes.

            
            * #### **Ingredient Based Recommendations**:
            The Ingredient Based Recommendations page is a great way to discover new cocktails based on the specific ingredients you're in the mood for. Simply enter one or more ingredients that you'd like to include in your cocktail, and our app will provide you with three personalized cocktail recommendations that match your preferences.
            
            We're excited to help you discover new and exciting cocktail recipes that you'll love. So go ahead, explore our app, and let us know if you have any questions or feedback. Below is a QR code to view the GitHub reposity which holds all our code if you're interested in learning about how this website was made. Cheers!
            '''
            ),

    ], style={'fontSize': '20px'}),
    html.Br(),
    html.Div([html.Img(src="assets/QR_Git.png", height="200px")], style={'textAlign':'center'})
])