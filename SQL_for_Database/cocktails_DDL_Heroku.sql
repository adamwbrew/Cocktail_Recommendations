CREATE SCHEMA `CocktailsData`;

-- DDL for Cocktails Database

-- initalize database
DROP DATABASE IF EXISTS CocktailsData;
CREATE DATABASE CocktailsData;
USE CocktailsData;

-- Reset Schema
DROP TABLE IF EXISTS Instructions_by_Drink;

DROP TABLE IF EXISTS Measured_Ingredients;

DROP TABLE IF EXISTS Recipes;

DROP TABLE IF EXISTS Ingredients;

DROP TABLE IF EXISTS Measurements;

DROP TABLE IF EXISTS Instructions;

DROP TABLE IF EXISTS Liquors;

DROP TABLE IF EXISTS Glassware;

DROP TABLE IF EXISTS Garnishes;

DROP TABLE IF EXISTS Sources;


CREATE TABLE Ingredients(
    IngredientID int primary key auto_increment,
    Ingredient_Name varchar(100) not null
);

CREATE TABLE Measurements(
    MeasurementID int primary key auto_increment,
    Measurement_Amount varchar(50) null
);

CREATE TABLE Instructions(
    InstructionID int primary key auto_increment,
    Instruction varchar(500) not null
);

CREATE TABLE Liquors(
    LiquorID int primary key auto_increment,
    Liquor_Name varchar(100) not null
);

CREATE TABLE Glassware(
    GlasswareID int primary key auto_increment,
    Glassware_Name varchar(100) not null
);

CREATE TABLE Garnishes(
    GarnishID int primary key auto_increment,
    Garnish_Name varchar(100) not null
);

CREATE TABLE Sources(
    SourceID int primary key auto_increment,
    Source varchar(250) not null
);

CREATE TABLE Recipes(
    RecipeID int primary key auto_increment,
    Cocktail_Name varchar(100) not null,
    LiquorID int not null, 
        constraint fk_Cocktails_Liquor foreign key (LiquorID) references Liquors(LiquorID),
    GlasswareID int not null, 
        constraint fk_Cocktails_Glassware foreign key (GlasswareID) references Glassware(GlasswareID),
    GarnishID int not null, 
        constraint fk_Cocktails_Garnish foreign key (GarnishID) references Garnishes(GarnishID),
    SourceID int not null, 
        constraint fk_Cocktails_Source foreign key (SourceID) references Sources(SourceID)
);

CREATE TABLE Instructions_by_Drink(
    Instructions_by_DrinkID int primary key auto_increment,
    InstructionID int not null, 
        constraint fk_Cocktails_Instruction foreign key (InstructionID) references Instructions(InstructionID),
    RecipeID int not null, 
        constraint fk_Cocktails_Recipe_1 foreign key (RecipeID) references Recipes(RecipeID)
);

CREATE TABLE Measured_Ingredients(
    Measured_IngredientID int primary key auto_increment,
    RecipeID int not null, 
        constraint fk_Cocktails_Recipe_2 foreign key (RecipeID) references Recipes(RecipeID),
    IngredientID int not null, 
        constraint fk_Cocktails_Ingredient foreign key (IngredientID) references Ingredients(IngredientID),
    MeasurementID int not null, 
        constraint fk_Cocktails_Measurement foreign key (MeasurementID) references Measurements(MeasurementID)
);


