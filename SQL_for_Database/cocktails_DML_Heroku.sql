-- DML for Cocktails Database

USE CocktailsData;

-- USE CocktailsData;
-- GO

-- DML Inserts

-- Measurements added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_1
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_1 = Measurements.Measurement_Amount);

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_2
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_2 = Measurements.Measurement_Amount)
    AND CD.Measurement_2 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_3
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_3 = Measurements.Measurement_Amount)
    AND CD.Measurement_3 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_4
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_4 = Measurements.Measurement_Amount)
    AND CD.Measurement_4 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_5
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_5 = Measurements.Measurement_Amount)
    AND CD.Measurement_5 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_6
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_6 = Measurements.Measurement_Amount)
    AND CD.Measurement_6 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_7
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_7 = Measurements.Measurement_Amount)
    AND CD.Measurement_7 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_8
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_8 = Measurements.Measurement_Amount)
    AND CD.Measurement_8 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_9
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_9 = Measurements.Measurement_Amount)
    AND CD.Measurement_9 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_10
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_10 = Measurements.Measurement_Amount)
    AND CD.Measurement_10 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_11
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_11 = Measurements.Measurement_Amount)
    AND CD.Measurement_11 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_12
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_12 = Measurements.Measurement_Amount)
    AND CD.Measurement_12 IS NOT NULL;

INSERT INTO Measurements(Measurement_Amount)
    SELECT DISTINCT Measurement_13
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Measurement_Amount
                        FROM Measurements
                        WHERE CD.Measurement_13 = Measurements.Measurement_Amount)
    AND CD.Measurement_13 IS NOT NULL;


-- Ingredients added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_1
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_1 = Ingredients.Ingredient_Name);

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_2
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_2 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_2 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_3
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_3 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_3 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_4
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_4 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_4 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_5
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_5 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_5 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_6
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_6 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_6 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_7
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_7 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_7 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_8
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_8 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_8 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_9
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_9 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_9 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_10
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_10 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_10 IS NOT NULL;

    INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_11
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_11 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_11 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_12
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_12 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_12 IS NOT NULL;

INSERT INTO Ingredients(Ingredient_Name)
    SELECT DISTINCT Ingredient_13
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Ingredient_Name
                        FROM Ingredients
                        WHERE CD.Ingredient_13 = Ingredients.Ingredient_Name)
    AND CD.Ingredient_13 IS NOT NULL;


-- Instructions added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_1
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_1 = Instructions.Instruction);

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_2
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_2 = Instructions.Instruction)
    AND CD.Instruction_2 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_3
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_3 = Instructions.Instruction)
    AND CD.Instruction_3 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_4
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_4 = Instructions.Instruction)
    AND CD.Instruction_4 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_5
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_5 = Instructions.Instruction)
    AND CD.Instruction_5 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_6
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_6 = Instructions.Instruction)
    AND CD.Instruction_6 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_7
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_7 = Instructions.Instruction)
    AND CD.Instruction_7 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_8
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_8 = Instructions.Instruction)
    AND CD.Instruction_8 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_9
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_9 = Instructions.Instruction)
    AND CD.Instruction_9 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_10
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_10 = Instructions.Instruction)
    AND CD.Instruction_10 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_11
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_11 = Instructions.Instruction)
    AND CD.Instruction_11 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_12
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_12 = Instructions.Instruction)
    AND CD.Instruction_12 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_13
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_13 = Instructions.Instruction)
    AND CD.Instruction_13 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_14
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_14 = Instructions.Instruction)
    AND CD.Instruction_14 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_15
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_15 = Instructions.Instruction)
    AND CD.Instruction_15 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_16
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_16 = Instructions.Instruction)
    AND CD.Instruction_16 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_17
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_17 = Instructions.Instruction)
    AND CD.Instruction_17 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_18
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_18 = Instructions.Instruction)
    AND CD.Instruction_18 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_19
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_19 = Instructions.Instruction)
    AND CD.Instruction_19 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_20
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_20 = Instructions.Instruction)
    AND CD.Instruction_20 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_21
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_21 = Instructions.Instruction)
    AND CD.Instruction_21 IS NOT NULL;

INSERT INTO Instructions(Instruction)
    SELECT DISTINCT Instruction_22
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Instruction
                        FROM Instructions
                        WHERE CD.Instruction_22 = Instructions.Instruction)
    AND CD.Instruction_22 IS NOT NULL;


-- Liquors added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Liquors(Liquor_Name)
    SELECT DISTINCT Liquor
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Liquor_Name
                        FROM Liquors
                        WHERE CD.Liquor = Liquors.Liquor_Name);


-- Glassware added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Glassware(Glassware_Name)
    SELECT DISTINCT Glassware
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Glassware_Name
                        FROM Glassware
                        WHERE CD.Glassware = Glassware.Glassware_Name);


-- Garnishes added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Garnishes(Garnish_Name)
    SELECT DISTINCT Garnish
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Garnish_Name
                        FROM Garnishes
                        WHERE CD.Garnish = Garnishes.Garnish_Name);


-- Sources added - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Sources(Source)
    SELECT DISTINCT Original_Source
    FROM Master.CocktailsDenormalized AS CD
    WHERE NOT EXISTS (SELECT Source
                        FROM Sources
                        WHERE CD.Original_Source = Sources.Source);


-- Recipe Added - - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Recipes(Cocktail_Name, LiquorID, GlasswareID, GarnishID, SourceID)
    SELECT 
        CD.Cocktail_Name,
        L.LiquorID,
        Gl.GlasswareID,
        G.GarnishID,
        S.SourceID
    FROM Master.CocktailsDenormalized AS CD
    INNER JOIN Liquors AS L ON CD.Liquor = L.Liquor_Name
    INNER JOIN Glassware AS Gl ON CD.Glassware = Gl.Glassware_Name
    INNER JOIN Garnishes AS G ON CD.Garnish = G.Garnish_Name
    INNER JOIN Sources AS S ON CD.Original_Source = S.Source;


-- Instructions_by_Drink Added - - - - - - - - - - - - - - - - - - - - - - - - - - 

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_1 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_2 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_3 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_4 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_5 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_6 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_7 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_8 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_9 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_10 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_11 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_12 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_13 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_14 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_15 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_16 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_18 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_19 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_20 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_21 = I.Instruction;

INSERT INTO Instructions_by_Drink(InstructionID, RecipeID)
    SELECT 
    I.InstructionID,
    R.RecipeID
    FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Instructions AS I ON CD.Instruction_22 = I.Instruction;


    -- Measured_Ingredients Added - - - - - - - - - - - - - - - - - - - - - - - - -
INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_1 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_1 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_2 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_2 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_3 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_3 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_4 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_4 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_5 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_5 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_6 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_6 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_7 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_7 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_8 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_8 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_9 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_9 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_10 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_10 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_11 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_11 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_12 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_12 = M.Measurement_Amount;

INSERT INTO Measured_Ingredients(RecipeID, IngredientID, MeasurementID)
    SELECT 
        R.RecipeID,
        I.IngredientID,
        M.MeasurementID
        FROM Recipes AS R
    INNER JOIN Liquors AS L ON R.LiquorID = L.LiquorID
    INNER JOIN Glassware AS Gl ON R.GlasswareID = Gl.GlasswareID
    INNER JOIN Garnishes AS G ON R.GarnishID = G.GarnishID
    INNER JOIN Sources AS S ON R.SourceID = S.SourceID
    INNER JOIN Master.CocktailsDenormalized AS CD ON R.Cocktail_Name = CD.Cocktail_Name 
        AND L.Liquor_Name = CD.Liquor 
        AND Gl.Glassware_Name = CD.Glassware 
        AND G.Garnish_Name = CD.Garnish
        AND S.Source = CD.Original_Source
    INNER JOIN Ingredients AS I ON CD.Ingredient_13 = I.Ingredient_Name
    INNER JOIN Measurements AS M ON CD.Measurement_13 = M.Measurement_Amount;