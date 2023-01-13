-- DDL for Cocktails Database

-- initial master database use statement
USE dmp84eqrjvyr1zp;
GO
-- Alter database CocktailsData SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
-- GO

-- -- initalize database
-- DROP DATABASE IF EXISTS CocktailsData;
-- GO
-- CREATE DATABASE CocktailsData;
-- GO
-- USE CocktailsData;
-- GO

-- Reset Schema
DROP TABLE Instructions_by_Drink;
GO

DROP TABLE Measured_Ingredients;
GO

DROP TABLE Recipes;
GO

DROP TABLE Ingredients;
GO

DROP TABLE Measurements;
GO

DROP TABLE Instructions;
GO

DROP TABLE Liquors;
GO

DROP TABLE Glassware;
GO

DROP TABLE Garnishes;
GO

DROP TABLE Sources;
GO


CREATE TABLE Ingredients(
    IngredientID int primary key identity(1,1),
    Ingredient_Name varchar(100) not null,
);
GO

CREATE TABLE Measurements(
    MeasurementID int primary key identity(1,1),
    Measurement_Amount varchar(50) null,
);
GO

CREATE TABLE Instructions(
    InstructionID int primary key identity(1,1),
    Instruction varchar(500) not null,
);
GO

CREATE TABLE Liquors(
    LiquorID int primary key identity(1,1),
    Liquor_Name varchar(100) not null,
);
GO

CREATE TABLE Glassware(
    GlasswareID int primary key identity(1,1),
    Glassware_Name varchar(100) not null,
);
GO

CREATE TABLE Garnishes(
    GarnishID int primary key identity(1,1),
    Garnish_Name varchar(100) not null,
);
GO

CREATE TABLE Sources(
    SourceID int primary key identity(1,1),
    Source varchar(250) not null
);
GO

CREATE TABLE Recipes(
    RecipeID int primary key identity(1,1),
    Cocktail_Name varchar(100) not null,
    LiquorID int not null, 
        constraint fk_Cocktails_Liquor foreign key (LiquorID) references [Liquors](LiquorID),
    GlasswareID int not null, 
        constraint fk_Cocktails_Glassware foreign key (GlasswareID) references [Glassware](GlasswareID),
    GarnishID int not null, 
        constraint fk_Cocktails_Garnish foreign key (GarnishID) references [Garnishes](GarnishID),
    SourceID int not null, 
        constraint fk_Cocktails_Source foreign key (SourceID) references [Sources](SourceID),
);
GO

CREATE TABLE Instructions_by_Drink(
    Instructions_by_DrinkID int primary key identity(1,1),
    InstructionID int not null, 
        constraint fk_Cocktails_Instruction foreign key (InstructionID) references [Instructions](InstructionID),
    RecipeID int not null, 
        constraint fk_Cocktails_Recipe_1 foreign key (RecipeID) references [Recipes](RecipeID),
);
GO

CREATE TABLE Measured_Ingredients(
    Measured_IngredientID int primary key identity(1,1),
    RecipeID int not null, 
        constraint fk_Cocktails_Recipe_2 foreign key (RecipeID) references [Recipes](RecipeID),
    IngredientID int not null, 
        constraint fk_Cocktails_Ingredient foreign key (IngredientID) references [Ingredients](IngredientID),
    MeasurementID int not null, 
        constraint fk_Cocktails_Measurement foreign key (MeasurementID) references [Measurements](MeasurementID),
);
GO


