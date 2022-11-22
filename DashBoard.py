import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import pymssql


# import SQL database connection strings - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from config import database
from config import username
from config import password
from config import server

from config import Garnishes
from config import Glassware
from config import Ingredients
from config import Instructions
from config import Instructions_by_Drink
from config import Liquors
from config import Measured_Ingredients
from config import Measurements
from config import Recipes
from config import Sources


try:
    conn = pymssql.connect(server,username, password,database)

    cursor = conn.cursor()
    query = f"""
    SELECT DISTINCT
        R.Cocktail_Name,
        L.Liquor_Name,
        Gl.Glassware_Name,
        G.Garnish_Name,
        S.Source,
        MI.Ingredients,
        I.Instructions
        FROM {Recipes} AS R
    INNER JOIN {Liquors} AS L ON R.LiquorID = L.LiquorID
    INNER JOIN {Glassware} AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN {Garnishes} AS G ON R.GarnishID = G.GarnishID
    INNER JOIN {Sources} AS S ON R.SourceID = S.SourceID
    -- Subquery of Measurements concatenated Ingredients in list form 
    INNER JOIN (SELECT DISTINCT
                R.Cocktail_Name,
                STRING_AGG(CONCAT(M.Measurement_Amount,' ', ING.Ingredient_Name), '&,& ') AS Ingredients
                FROM {Recipes} AS R
            INNER JOIN {Liquors} AS L ON R.LiquorID = L.LiquorID
            INNER JOIN {Measured_Ingredients} AS MI ON R.RecipeID = MI.RecipeID
            INNER JOIN {Ingredients} AS ING ON MI.IngredientID = ING.IngredientID
            INNER JOIN {Measurements} AS M ON MI.MeasurementID = M.MeasurementID
            GROUP BY R.Cocktail_Name)
        AS MI ON R.Cocktail_Name = MI.Cocktail_Name
    -- Subquery of Instructions in list form 
    INNER JOIN (SELECT DISTINCT
                R.Cocktail_Name,
                STRING_AGG(I.Instruction, '&,& ') WITHIN GROUP (ORDER BY I.Instruction) AS Instructions
                FROM {Recipes} AS R
            INNER JOIN {Instructions_by_Drink} AS ID ON R.RecipeID = ID.RecipeID
            INNER JOIN {Instructions} AS I ON ID.InstructionID = I.InstructionID
            GROUP BY R.Cocktail_Name)
        AS I ON R.Cocktail_Name = I.Cocktail_Name
    ORDER BY R.Cocktail_Name ASC;
    """
    Cocktails = pd.read_sql(query, conn)
except Exception as e:
    print(e)

Cocktails["Cocktail_Name"] = Cocktails["Cocktail_Name"].astype(str)
Cocktails["Liquor_Name"] = Cocktails["Liquor_Name"].astype(str)
Cocktails["Glassware_Name"] = Cocktails["Glassware_Name"].astype(str)
Cocktails["Garnish_Name"] = Cocktails["Garnish_Name"].astype(str)
Cocktails["Source"] = Cocktails["Source"].astype(str)
Cocktails["Ingredients"] = Cocktails.apply(lambda x : x["Ingredients"].split("&,& "), axis = 1)
Cocktails["Instructions"] = Cocktails.apply(lambda x : x["Instructions"].split("&,& "), axis = 1)

# DashBoard - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# link fontawesome 
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA])
server = app.server


cocktail_names = list(set(Cocktails["Cocktail_Name"].tolist()))
cocktail_names.sort()


app.layout = html.Div(children=[
    html.H1(children='Cocktail Recommendations', style={'textAlign': 'center', 'font-size': '50px', 'text-decoration': 'underline', 'margin-bottom':25, 'margin-top':25}),
    # Cocktail Relay System
    html.Div([
        dcc.Dropdown(options=cocktail_names,
                        placeholder = "Select or Search for Cocktail",
                        value= None,  # initial value displayed when page first loads
                        clearable=False,
                        searchable = True,
                        id = "dropdown_cocktail"),
    ]),
    html.Br(),
    html.P(id = "Cocktail_Output"),
    html.P(id = "Liquor_Output"),
    html.P(id = "Ingredients_Output"),
    html.P(id = "Instructions_Output"),
    html.P(id = "Glassware_Output"),
    html.P(id = "Garnish_Output"),
    html.P(id = "Source_Output")

])


@app.callback(
    Output("Cocktail_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        cocktail = mini_df['Cocktail_Name'].iloc[0]
        output += f"Cocktail: {cocktail}"
    return output


@app.callback(
    Output("Liquor_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        liquor = mini_df['Liquor_Name'].iloc[0]
        output += f"Liquor: {liquor}"
    return output


@app.callback(
    Output("Ingredients_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = ["Ingredients:", html.Br()]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        ingredients = mini_df['Ingredients'].iloc[0]
        for i in range(len(ingredients)):
            output +=  [f"{ingredients[i]}"]
            output +=  [html.Br()]
    return output


@app.callback(
    Output("Instructions_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        output = ["Instructions:", html.Br()]
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        instructions = mini_df['Instructions'].iloc[0]
        for i in range(len(instructions)):
            output +=  [f"{instructions[i]}"]
            output +=  [html.Br()]
    return output


@app.callback(
    Output("Glassware_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        glassware = mini_df['Glassware_Name'].iloc[0]
        output += f"Glassware: {glassware}"
    return output


@app.callback(
    Output("Garnish_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        garnish = mini_df['Garnish_Name'].iloc[0]
        output += f"Garnsih: {garnish}"
    return output


@app.callback(
    Output("Source_Output", component_property = "children"),
    Input("dropdown_cocktail", component_property = "value")
)
def cocktail_output(user_input):
    output = ""
    if(user_input == None):
        output = None
    else:
        mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{user_input}"]
        source = mini_df['Source'].iloc[0]
        output += f"Source: {source}"
    return output


if __name__ == '__main__':
    app.run_server(debug=True)