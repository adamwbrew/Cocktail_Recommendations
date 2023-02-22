import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html, callback
import dash_html_components as html
import pandas as pd
import pymssql
import os
import pymysql.cursors

# import SQL database connection strings - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# If we are in production, make sure we DO NOT use the debug mode
if os.environ.get('ENV') == 'production':
    # Heroku gives us an environment variable called DATABASE_URL when we add a postgres database
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    database =  os.environ.get('DATABASE')
    username =  os.environ.get('USERNAME')
    password =  os.environ.get('PASSWORD')
    server =  os.environ.get('SERVER')

else:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-heroku'
    # import SQL database connection strings
    from pages.secrets import database
    from pages.secrets import username
    from pages.secrets import password
    from pages.secrets import server

from pages.config import Garnishes
from pages.config import Glassware
from pages.config import Ingredients
from pages.config import Instructions
from pages.config import Instructions_by_Drink
from pages.config import Liquors
from pages.config import Measured_Ingredients
from pages.config import Measurements
from pages.config import Recipes
from pages.config import Sources



# Tables needed - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
try:
    conn = pymysql.connect(host=f"{server}",
                                         database=f"{database}",
                                         user=f"{username}",
                                         password=f"{password}")

    cursor = conn.cursor()
    query = f"""
    SELECT DISTINCT
        R.RecipeID,
        R.Cocktail_Name,
        L.Liquor_Name,
        Gl.Glassware_Name,
        G.Garnish_Name,
        S.Source,
        MI.Ingredients_List,
        MI.IngredientsID_List,
        MI.Ingredients,
        I.Instructions
        FROM {Recipes} AS R
    INNER JOIN {Liquors} AS L ON R.LiquorID = L.LiquorID
    INNER JOIN {Glassware} AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN {Garnishes} AS G ON R.GarnishID = G.GarnishID
    INNER JOIN {Sources} AS S ON R.SourceID = S.SourceID
    -- Subquery of Measurements concatenated Ingredients in list form 
    INNER JOIN (SELECT DISTINCT
                R.RecipeID,
                R.Cocktail_Name,
                GROUP_CONCAT(DISTINCT ING.Ingredient_Name ORDER BY ING.Ingredient_Name SEPARATOR '&,& ') AS Ingredients_List,
                GROUP_CONCAT(DISTINCT ING.IngredientID ORDER BY ING.IngredientID SEPARATOR '&,& ') AS IngredientsID_List,
                GROUP_CONCAT(DISTINCT CONCAT(M.Measurement_Amount,' ', ING.Ingredient_Name) SEPARATOR '&,& ') AS Ingredients
                FROM {Recipes} AS R
            INNER JOIN {Liquors} AS L ON R.LiquorID = L.LiquorID
            INNER JOIN {Measured_Ingredients} AS MI ON R.RecipeID = MI.RecipeID
            INNER JOIN {Ingredients} AS ING ON MI.IngredientID = ING.IngredientID
            INNER JOIN {Measurements} AS M ON MI.MeasurementID = M.MeasurementID
            GROUP BY R.RecipeID, R.Cocktail_Name)
        AS MI ON R.Cocktail_Name = MI.Cocktail_Name
    -- Subquery of Instructions in list form 
    INNER JOIN (SELECT DISTINCT
                R.RecipeID,
                R.Cocktail_Name,
                GROUP_CONCAT(DISTINCT I.Instruction ORDER BY I.Instruction SEPARATOR '&,& ') AS Instructions
                FROM {Recipes} AS R
            INNER JOIN {Instructions_by_Drink} AS ID ON R.RecipeID = ID.RecipeID
            INNER JOIN {Instructions} AS I ON ID.InstructionID = I.InstructionID
            GROUP BY R.RecipeID, R.Cocktail_Name)
        AS I ON R.Cocktail_Name = I.Cocktail_Name
    ORDER BY R.RecipeID, R.Cocktail_Name ASC;
    """
    Cocktails = pd.read_sql(query, conn)
except pymysql.Error as e:
    print("Error while connecting to MySQL", e)

Cocktails["Cocktail_Name"] = Cocktails["Cocktail_Name"].astype(str)
Cocktails["Liquor_Name"] = Cocktails["Liquor_Name"].astype(str)
Cocktails["Glassware_Name"] = Cocktails["Glassware_Name"].astype(str)
Cocktails["Garnish_Name"] = Cocktails["Garnish_Name"].astype(str)
Cocktails["Source"] = Cocktails["Source"].astype(str)
Cocktails["Ingredients"] = Cocktails.apply(lambda x : x["Ingredients"].split("&,& "), axis = 1)
Cocktails["Instructions"] = Cocktails.apply(lambda x : x["Instructions"].split("&,& "), axis = 1)

# app - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# link fontawesome 
dash.register_page(__name__, path='/Search')

cocktail_names = list(set(Cocktails["Cocktail_Name"].tolist()))
cocktail_names.sort()


# app for cocktail search with all information formatted
layout = html.Div(children=[
    html.H1(children='Search for a Cocktail', style={'textAlign': 'center','margin-bottom':25, 'margin-top':25}),
    html.P(children = "This page  is a powerful tool that allows you to search through our comprehensive database of cocktail recipes. You'll find information on the main liquor used, a list of ingredients, instructions on how to make the cocktail, preferred glassware, garnishes, and the source of the recipe, if known.", style={'fontSize': '20px'}),
    # Cocktail Relay System
    html.Div([
        dcc.Dropdown(options=cocktail_names,
                        placeholder = "Select or Search for Cocktail",
                        value= None,  # initial value displayed when page first loads
                        clearable=False,
                        searchable = True,
                        style={"backgroundColor": "white", "color": "black"},
                        id = "dropdown_cocktail"),
    ]),
    html.Br(),
    html.Div(id = "Cocktail_Output"),
    html.Div(id = "Liquor_Output"),
    html.Div(id = "Ingredients_Output"),
    html.Div(id = "Instructions_Output"),
    html.Div(id = "Glassware_Output"),
    html.Div(id = "Garnish_Output"),
    html.Div(id = "Source_Output")

])

# Basic Cocktail Search Callbacks - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
@callback(
    Output("Cocktail_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Cocktail:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        cocktail = mini_df['Cocktail_Name'].iloc[0]
        output += [html.P(children = f"{cocktail}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
    return output


@callback(
    Output("Liquor_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Liquor:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        liquor = mini_df['Liquor_Name'].iloc[0]
        output += [html.P(children = f"{liquor}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
    return output


@callback(
    Output("Ingredients_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Ingredients:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        ingredients = mini_df['Ingredients'].iloc[0]
        for i in range(len(ingredients)):
            output += [html.P(children = f"{ingredients[i]}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
            output +=  [html.Br()]
    return output


@callback(
    Output("Instructions_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Instructions:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        instructions = mini_df['Instructions'].iloc[0]
        for i in range(len(instructions)):
            output += [html.P(children = f"{instructions[i]}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
            output +=  [html.Br()]
    return output


@callback(
    Output("Glassware_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Glassware:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        glassware = mini_df['Glassware_Name'].iloc[0]
        output += [html.P(children = f"{glassware}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
    return output


@callback(
    Output("Garnish_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Garnish:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        garnish = mini_df['Garnish_Name'].iloc[0]
        output += [html.P(children = f"{garnish}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
    return output


@callback(
    Output("Source_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = [html.H2(children='Source:', style = {'text-decoration': 'underline', 'margin-left':40, 'margin-right':40, 'font-size': '40px'})]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        source = mini_df['Source'].iloc[0]
        output += [html.P(children = f"{source}", style = {'margin-left':50, 'margin-right':50, 'font-size': '30px'})]
    return output
