USE CocktailsData;

SELECT * From Ingredients WHERE Ingredient_Name = ''; 
-- Ingredient_ID = 1031

SELECT * From Instructions WHERE Instruction = ''; 
-- Instruction_ID = 2049

-- adjust based on table IDs
DELETE FROM Measured_Ingredients WHERE Measured_Ingredients.IngredientID = 1031;
DELETE FROM Ingredients WHERE Ingredients.IngredientID = 1031;
DELETE FROM Instructions_by_Drink WHERE Instructions_by_Drink.InstructionID = 2049;
DELETE FROM Instructions WHERE Instructions.InstructionID = 2049;