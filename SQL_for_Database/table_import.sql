USE Master;

DROP TABLE IF EXISTS CocktailsDenormalized;


CREATE TABLE CocktailsDenormalized(
    Cocktail_Name text not null,
    Liquor text not null,
    Garnish text not null,
    Glassware text not null,
    Original_Source text not null,
    Ingredient_1 text null,
    Measurement_1 text null,
    Ingredient_2 text null,
    Measurement_2 text null,
    Ingredient_3 text null,
    Measurement_3 text null,
    Ingredient_4 text null,
    Measurement_4 text null,
    Ingredient_5 text null,
    Measurement_5 text null,
    Ingredient_6 text null,
    Measurement_6 text null,
    Ingredient_7 text null,
    Measurement_7 text null,
    Ingredient_8 text null,
    Measurement_8 text null,
    Ingredient_9 text null, 
    Measurement_9 text null,
    Ingredient_10 text null,
    Measurement_10 text null,
    Ingredient_11 text null,
    Measurement_11 text null,
    Ingredient_12 text null,
    Measurement_12 text null,
    Ingredient_13 text null,
    Measurement_13 text null,
    Instruction_1 text null,
    Instruction_2 text null,
    Instruction_3 text null, 
    Instruction_4 text null,
    Instruction_5 text null,
    Instruction_6 text null,
    Instruction_7 text null, 
    Instruction_8 text null,
    Instruction_9 text null,
    Instruction_10 text null,
    Instruction_11 text null,
    Instruction_12 text null,
    Instruction_13 text null, 
    Instruction_14 text null,
    Instruction_15 text null,
    Instruction_16 text null,
    Instruction_17 text null,
    Instruction_18 text null,
    Instruction_19 text null, 
    Instruction_20 text null, 
    Instruction_21 text null, 
    Instruction_22 text null,
    Instruction_23 text null
);

LOAD DATA LOCAL INFILE  
'C:/Users/Adam Brewer/Desktop/Cocktail_Recommendations/Datasets_Nonnormalized/cocktails.csv'
INTO TABLE CocktailsDenormalized  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;