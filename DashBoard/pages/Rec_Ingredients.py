import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html, callback
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import pymssql


# import SQL database connection strings - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from pages.config import database
from pages.config import username
from pages.config import password
from pages.config import server

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
    conn = pymssql.connect(server,username, password,database)

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
                STRING_AGG(ING.Ingredient_Name, '&,& ') AS Ingredients_List,
                STRING_AGG(ING.IngredientID, '&,& ') AS IngredientsID_List,
                STRING_AGG(CONCAT(M.Measurement_Amount,' ', ING.Ingredient_Name), '&,& ') AS Ingredients
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
                STRING_AGG(I.Instruction, '&,& ') WITHIN GROUP (ORDER BY I.Instruction) AS Instructions
                FROM {Recipes} AS R
            INNER JOIN {Instructions_by_Drink} AS ID ON R.RecipeID = ID.RecipeID
            INNER JOIN {Instructions} AS I ON ID.InstructionID = I.InstructionID
            GROUP BY R.RecipeID, R.Cocktail_Name)
        AS I ON R.Cocktail_Name = I.Cocktail_Name
    ORDER BY R.RecipeID, R.Cocktail_Name ASC;
    """
    Cocktails = pd.read_sql(query, conn)
except Exception as e:
    print(e)


try:
    conn = pymssql.connect(server,username, password,database)

    cursor = conn.cursor()
    Ingredient_query = f"""
    SELECT DISTINCT
        ING.Ingredient_Name
        FROM {Ingredients} AS ING
    ORDER BY ING.Ingredient_Name ASC
    """
    Ingredient_query = pd.read_sql(Ingredient_query, conn)
except Exception as e:
    print(e)


Cocktails["Cocktail_Name"] = Cocktails["Cocktail_Name"].astype(str)
Cocktails["Liquor_Name"] = Cocktails["Liquor_Name"].astype(str)
Cocktails["Glassware_Name"] = Cocktails["Glassware_Name"].astype(str)
Cocktails["Garnish_Name"] = Cocktails["Garnish_Name"].astype(str)
Cocktails["Source"] = Cocktails["Source"].astype(str)
Cocktails["Ingredients_List"] = Cocktails.apply(lambda x : x["Ingredients_List"].split("&,& "), axis = 1)
Cocktails["IngredientsID_List"] = Cocktails.apply(lambda x : x["IngredientsID_List"].split("&,& "), axis = 1)
Cocktails["Ingredients"] = Cocktails.apply(lambda x : x["Ingredients"].split("&,& "), axis = 1)
Cocktails["Instructions"] = Cocktails.apply(lambda x : x["Instructions"].split("&,& "), axis = 1)

# needed functions for pattern matching - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def list_breakdown(list_):
    result = []
    for i in list_:
        i = i.strip()
        if(i == ""):continue
        else: result += i.split(" ")
    return result

def Similarity_Added_labels(df_drinks, drink_ingredients_list):

    def Similarity_Measure(other_ingredient_list, drink_ingredient_list):
        drink_1 = list_breakdown(list(map(str, other_ingredient_list)))
        drink_2 = list_breakdown(list(map(str, drink_ingredient_list)))
        measure = 0
        for num in drink_2:
            if(num.title() in drink_1):
                measure += 1 
        return measure

    drink_ingredients_list = list(set(list(map(str.strip, drink_ingredients_list))))
    df_drinks["Similarity"] = df_drinks.apply(lambda x : Similarity_Measure(x["Ingredients_List"], drink_ingredients_list), axis = 1)
    df_drinks = df_drinks.sort_values(by = "Similarity", ascending = False)
    max_measure = df_drinks["Similarity"].max()
    df_drinks_sim = df_drinks[df_drinks["Similarity"] == max_measure]
    # extra constaints based on resulting similarities df
    if(max_measure == 0):
        return None
    else:
        similarity_count_df = pd.DataFrame(df_drinks["Similarity"].value_counts()).sort_values(by="Similarity", ascending= False)
        num_sim_cocktails = similarity_count_df.tail(1)["Similarity"].reset_index().drop(["index"], axis = 1).loc[similarity_count_df.index[0]]["Similarity"]
        if(num_sim_cocktails == 3):
            return df_drinks_sim
        else:
            if(num_sim_cocktails < 3):
                for i in range(1,max_measure+1):
                    other_drinks = df_drinks[df_drinks["Similarity"] == (max_measure - i)]
                    if(len(other_drinks) == 0): continue
                    else: break
                return pd.concat([df_drinks_sim, other_drinks.sample(3 - num_sim_cocktails)], axis=0)
            else:
                return df_drinks_sim.sample(3)

# app - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# link fontawesome 
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
dash.register_page(__name__, path='/Ingredient_based_Recommendation')

cocktail_names = list(set(Cocktails["Cocktail_Name"].tolist()))
cocktail_names.sort()

Ingredient_query = list(set(Ingredient_query["Ingredient_Name"].tolist()))
Ingredient_query.sort()

# app for cocktail search with all information formatted
layout = html.Div(children=[
    html.H1(children='Ingredient Based Recommendations', style={'textAlign': 'center', 'font-size': '50px', 'text-decoration': 'underline', 'margin-bottom':25, 'margin-top':25}),
    # Cocktail Relay System
    html.Div([
        dcc.Textarea(
        id='textarea-state-example',
        placeholder='If specific ingredients are not found in dropdown menu above \nplease type them in here with commas separating the ingredients.\nFor example: Cherry, Lime, Vodka',
        style={'width': '100%', 'height': 80},
        ),
        html.Button('Submit', id='textarea-state-example-button', n_clicks=0),
        html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})

    ])
])

def list_formatter(list_):
    list_.sort()
    result = "\n"
    for i in list_:
        i = i.strip()
        if(i == ""):continue
        else:
            result += str(i).title() + "\n"
    return result

@callback(
    Output('textarea-state-example-output', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),
    State('textarea-state-example', 'value')
)
def update_output(n_clicks, value_1):
    if n_clicks > 0:
        if(value_1 == None):
            return f"\nYou have entered: \nNo ingredients have been entered yet."
        else:
            value_1 = value_1.strip()
            if(value_1 == [] or value_1 == None or value_1 ==""):
                return f"\nYou have entered: \nNo ingredients have been entered yet."
            else:
                ingrdient_list = value_1.split(",")
                ingrdient_list = list(set(list(map(str.strip, ingrdient_list))))
                recommendations = Similarity_Added_labels(Cocktails, ingrdient_list)
                if isinstance(recommendations, type(None)):
                    return f"\nYou have entered: (with duplicates removed){list_formatter(ingrdient_list)}"
                else: 
                    return f"\nYou have entered: (with duplicates removed){list_formatter(ingrdient_list)}"  

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
# columns output for drinks