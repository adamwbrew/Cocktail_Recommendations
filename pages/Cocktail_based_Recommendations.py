import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html, callback
import pandas as pd
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


try:
    conn = pymysql.connect(host=f"{server}",
                                         database=f"{database}",
                                         user=f"{username}",
                                         password=f"{password}")


    cursor = conn.cursor()
    Ingredient_query = f"""
    SELECT DISTINCT
        ING.Ingredient_Name
        FROM {Ingredients} AS ING
    ORDER BY ING.Ingredient_Name ASC
    """
    Ingredient_query = pd.read_sql(Ingredient_query, conn)
except pymysql.Error as e:
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

def Similarity_Added_labels_Cocktail(df_drinks, drink_ingredients_list, cocktail_names):

    def Similarity_Measure(other_ingredient_list, drink_ingredient_list):
        drink_1 = list_breakdown(list(map(str, other_ingredient_list)))
        drink_2 = list_breakdown(list(map(str, drink_ingredient_list)))
        measure = 0
        for num in drink_2:
            if(num.title() in drink_1):
                measure += 1 
        return measure
        
    for cocktail in cocktail_names:
        df_drinks = df_drinks[df_drinks["Cocktail_Name"] != f"{cocktail}"]
    df_drinks["Similarity"] = df_drinks.apply(lambda x : Similarity_Measure(x["Ingredients_List"], drink_ingredients_list), axis = 1)
    df_drinks = df_drinks.sort_values(by = "Similarity", ascending = False)
    max_measure = df_drinks["Similarity"].max()
    df_drinks_sim = df_drinks[df_drinks["Similarity"] == max_measure]
    # extra constaints based on resulting similarities df
    if(max_measure == 0):
        return None
    else:
        similarity_count_df = pd.DataFrame(df_drinks["Similarity"].value_counts()).reset_index().sort_values(by="index", ascending= False)
        num_sim_cocktails = similarity_count_df.head(1)["Similarity"].tolist()[0]
        if(num_sim_cocktails == 3):
            return df_drinks_sim
        else:
            if(num_sim_cocktails < 3):
                # Finds 3 drinks based on similarity measure
                other_drinks = df_drinks.sample(0)
                for i in range(1,max_measure+1):
                    other_drinks = pd.concat([other_drinks, df_drinks[df_drinks["Similarity"] == (max_measure - i)]], axis=0)
                    if(len(other_drinks) < 3): continue
                    else: break
                # Returns 3 drinks in order of similarity measure
                result_df_ranked = df_drinks_sim
                for i in range(1,max_measure+1):
                    if(len(result_df_ranked) == 3):break
                    elif(len(result_df_ranked) < 3):
                        if(len(other_drinks[other_drinks["Similarity"] == (max_measure - i)]) >= 1):
                            if(len(other_drinks[other_drinks["Similarity"] == (max_measure - i)]) == 1):
                                result_df_ranked = pd.concat([result_df_ranked, other_drinks[other_drinks["Similarity"] == (max_measure - i)].sample(1)], axis=0)
                            else:
                                result_df_ranked = pd.concat([result_df_ranked, other_drinks[other_drinks["Similarity"] == (max_measure - i)].sample(3-len(result_df_ranked))], axis=0)
                        else:
                            # this is when the other_drinks has length 0, meaning we can bypass it sense it has no information
                            continue
                    
                return result_df_ranked
            else:
                return df_drinks_sim.sample(3)

# app - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# link fontawesome 
dash.register_page(__name__, path='/Cocktail_based_Recommendation')

cocktail_names = list(set(Cocktails["Cocktail_Name"].tolist()))
cocktail_names.sort()

# CSS styles for the container div
button_container_style = {
    "position": "relative",  # make the position relative
    "padding-top": "30px"
}

# Updated layout with the button and dropdown wrapped in a single container div
layout = html.Div(children=[
    html.H1(children='Cocktail Based Recommendations', style={'textAlign': 'center', 'margin-bottom':25, 'margin-top':25}),
    dcc.Markdown('''
                This page lets you easily find new cocktail recommendations based on your existing preferences. Simply input one or more cocktails that you already enjoy, and our app will generate three personalized cocktail recommendations tailored to your tastes. You can select up to three cocktails from the dropdown menu. 

                In addition to generating personalized cocktail recommendations, our app also allows you to manage your cocktail list with ease. You can delete any added cocktail by simply clicking the small blue X next to it. Alternatively, you can delete the entire cocktail by using the delete button on your keyboard. To clear all cocktails selected, click the small white X on the right of the dropdown menu.

                To further enhance your user experience, we've included a filter function that allows you to search for specific cocktails based on text filter. Simply add your desired text to the dropdown menu, and our app will show you only the cocktails that match your search criteria. This makes it easier for you to find the perfect cocktail to enjoy at any time. Try it out now and discover your new favorite cocktails!
                ''',
                style={'fontSize': '20px'}),
    # Cocktail Relay System
    html.Div([
        # Container div for dropdown and button
        html.Div([
            # Drop down for cocktails
            dcc.Dropdown(options=cocktail_names,
                            placeholder = "Select or Search for Cocktail",
                            value= None,  # initial value displayed when page first loads
                            clearable=True,  # allow users to clear their selection
                            searchable = True,
                            multi = True,
                            style={"fontSize": "15px", "height": "100px", "width":"100%"},
                            id = "dropdown_cocktail_CR")], style = {"display":"flex"}),
            # Button container div
            html.Div([
                dbc.Button("Click me", id="dropdown-state-example-button", color="info", className="me-1", n_clicks=0),
            ], id="dropdown-state-example-button-container", style=button_container_style),
        html.Div(id='dropdown-state-example-output', style={'whiteSpace': 'pre-line'})
    ])
])

# Callback function to limit the number of selected items to three
@callback(
    Output("dropdown_cocktail_CR", "value"),
    Input("dropdown_cocktail_CR", "value")
)
def limit_selection(value):
    if value is None:
        return value
    if len(value) > 3:
        return value[:3]
    else:
        return value
    

def list_formatter(list_):
    list_.sort()
    result = "\n"
    for i in list_:
        i = i.strip()
        if(i == ""):continue
        else:
            result += str(i).title() + "\n"
    return result

def sort_instructions(instructions):
    output = []
    unknown_step = []
    for intruction in instructions:
        prep_test = intruction.split(":")[0].lower()
        if(prep_test == "prep"):
            output.append(intruction)
        elif(prep_test.isdigit() == False):
            if(unknown_step == []):
                unknown_step.append("Steps included but with unknown order:")
            unknown_step.append(intruction)
    removed_prep = instructions.copy()
    if(output != []):
        removed_prep.remove(output[0])
    if(unknown_step[1:] != []):
        for i in unknown_step[1:]:
            removed_prep.remove(i)
    removed_prep.sort(key = lambda x : x.split(":")[0].zfill(2))
    for instruction in removed_prep:
        output.append(instruction)
    output += unknown_step
    return output

@callback(
    Output('dropdown-state-example-output', 'children'),
    Input('dropdown-state-example-button', 'n_clicks'),
    State('dropdown_cocktail_CR', 'value')
)
def update_output(n_clicks, value_1):
    if n_clicks > 0:

        if(value_1 == None):
            return f"\nYou have entered: \nNo cocktails have been entered yet."

        else:
            mini_df = Cocktails.sample(0)
            for i in value_1:
                mini_df = Cocktails[Cocktails["Cocktail_Name"] == f"{i}"]
            mini_df_ingredients_list = mini_df["Ingredients_List"].tolist()
            cocktail_ingredient_list = []
            for i in mini_df_ingredients_list:
                for j in i:
                    cocktail_ingredient_list += [j]

            recommendations = Similarity_Added_labels_Cocktail(Cocktails, cocktail_ingredient_list, value_1)
            if isinstance(recommendations, type(None)):
                return f"\nYou have entered: (with duplicates removed){list_formatter(cocktail_ingredient_list)}\n \nUnfortunately no coktails were found with the ingredients you inputted."
            else: 
                # Output cocktail Setup - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                Cocktail_Names = recommendations["Cocktail_Name"].tolist()
                Liquor_Names = recommendations["Liquor_Name"].tolist()
                Garnish_Names = recommendations["Garnish_Name"].tolist()
                Source_Names = recommendations["Source"].tolist()
                Glassware_Names = recommendations["Glassware_Name"].tolist()
                Ingredients_Names = recommendations["Ingredients"].tolist()
                Instructions_Names = recommendations["Instructions"].tolist()

                output_Ingredients_1 = [html.H2("Ingredients")]
                for i in range(len(Ingredients_Names[0])):
                    output_Ingredients_1 += [html.P(children = f"{Ingredients_Names[0][i]}")]
                output_Instructions_1 = [html.H2("Instructions")]
                Instructions_Names[0] = sort_instructions(Instructions_Names[0])
                for i in range(len(Instructions_Names[0])):
                    output_Instructions_1 += [html.P(children = f"{Instructions_Names[0][i]}")]

                output_Ingredients_2 = [html.H2("Ingredients")]
                for i in range(len(Ingredients_Names[1])):
                    output_Ingredients_2 += [html.P(children = f"{Ingredients_Names[1][i]}")]
                output_Instructions_2 = [html.H2("Instructions")]
                Instructions_Names[1] = sort_instructions(Instructions_Names[1])
                for i in range(len(Instructions_Names[1])):
                    output_Instructions_2 += [html.P(children = f"{Instructions_Names[1][i]}")]

                output_Ingredients_3 = [html.H2("Ingredients")]
                for i in range(len(Ingredients_Names[2])):
                    output_Ingredients_3 += [html.P(children = f"{Ingredients_Names[2][i]}")]
                output_Instructions_3 = [html.H2("Instructions")]
                Instructions_Names[2] = sort_instructions(Instructions_Names[2])
                for i in range(len(Instructions_Names[2])):
                    output_Instructions_3 += [html.P(children = f"{Instructions_Names[2][i]}")]


                output_Source_1 = [html.H2("Source")]
                if("," in Source_Names[0]):
                    Source_Names[0] = Source_Names[0].split(",")
                    for i in Source_Names[0]:
                        if(i == "Unknown"):continue
                        elif(i[-4:] == ".com"):
                            output_Source_1 += [html.P(children = f"Website{i[(i.find(':')):]}")]
                        else:
                            output_Source_1 += [html.P(children = f"{i}")]
                elif(Source_Names[0][-4:] == ".com"):
                    output_Source_1 += [html.P(children = f"Website{Source_Names[0][(Source_Names[0].find(':')):]}")]
                else: 
                    output_Source_1 += [html.P(children = f"{Source_Names[0]}")]


                output_Source_2 = [html.H2("Source")]
                if("," in Source_Names[1]):
                    Source_Names[1] = Source_Names[1].split(",")
                    for i in Source_Names[1]:
                        if(i == "Unknown"):continue
                        elif(i[-4:] == ".com"):
                            output_Source_2 += [html.P(children = f"Website{i[(i.find(':')):]}")]
                        else:
                            output_Source_2 += [html.P(children = f"{i}")]
                elif(Source_Names[1][-4:] == ".com"):
                    output_Source_2 += [html.P(children = f"Website{Source_Names[1][(Source_Names[1].find(':')):]}")]
                else: 
                    output_Source_2 += [html.P(children = f"{Source_Names[1]}")]


                output_Source_3 = [html.H2("Source")]
                if("," in Source_Names[2]):
                    Source_Names[2] = Source_Names[2].split(",")
                    for i in Source_Names[2]:
                        if(i == "Unknown"):continue
                        elif(i[-4:] == ".com"):
                            output_Source_3 += [html.P(children = f"Website{i[(i.find(':')):]}")]
                        else:
                            output_Source_3 += [html.P(children = f"{i}")]
                elif(Source_Names[2][-4:] == ".com"):
                    output_Source_3 += [html.P(children = f"Website{Source_Names[2][(Source_Names[2].find(':')):]}")]
                else: 
                    output_Source_3 += [html.P(children = f"{Source_Names[2]}")]


                row_break = html.Div(html.Hr(style={'borderWidth': "0.25vh", "width": "100%", "color": "#FFFFFF", 'textAlign': 'center'}))
                input = html.P(children=f"\nYou have entered: (with duplicates removed){list_formatter(value_1)}" , style={'font-size': '15px', 'margin-bottom':25, 'margin-top':25})
                header_1 = html.H1(children=f'{Cocktail_Names[0]}', style={'textAlign': 'center', 'margin-bottom':25, 'margin-top':25})
                row_1 = html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div([html.H2("Liquor"), html.P(f"{Liquor_Names[0]}")])),
                                dbc.Col(html.Div([html.H2("Garnish"), html.P(f"{Garnish_Names[0]}")])),
                                dbc.Col(html.Div([html.H2("Glassware"), html.P(f"{Glassware_Names[0]}")])),
                                dbc.Col(html.Div(output_Source_1)),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(output_Ingredients_1)),
                                dbc.Col(html.Div(output_Instructions_1)),
                            ]
                        ),
                    ]
                )
                header_2 = html.H1(children=f'{Cocktail_Names[1]}', style={'textAlign': 'center', 'margin-bottom':25, 'margin-top':25})
                row_2 = html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div([html.H2("Liquor"), html.P(f"{Liquor_Names[1]}")])),
                                dbc.Col(html.Div([html.H2("Garnish"), html.P(f"{Garnish_Names[1]}")])),
                                dbc.Col(html.Div([html.H2("Glassware"), html.P(f"{Glassware_Names[1]}")])),
                                dbc.Col(html.Div(output_Source_2)),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(output_Ingredients_2)),
                                dbc.Col(html.Div(output_Instructions_2)),
                            ]
                        ),
                    ]
                )
                header_3 = html.H1(children=f'{Cocktail_Names[2]}', style={'textAlign': 'center', 'margin-bottom':25, 'margin-top':25})
                row_3 = html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div([html.H2("Liquor"), html.P(f"{Liquor_Names[2]}")])),
                                dbc.Col(html.Div([html.H2("Garnish"), html.P(f"{Garnish_Names[2]}")])),
                                dbc.Col(html.Div([html.H2("Glassware"), html.P(f"{Glassware_Names[2]}")])),
                                dbc.Col(html.Div(output_Source_3)),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.Div(output_Ingredients_3)),
                                dbc.Col(html.Div(output_Instructions_3)),
                            ]
                        ),
                    ]
                )
                result =  html.Div([input, row_break, header_1, row_1, row_break,
                                                        header_2, row_2, row_break,
                                                        header_3, row_3, row_break])
                return result 