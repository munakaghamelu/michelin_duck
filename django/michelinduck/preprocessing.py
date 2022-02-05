import pandas as pd
import numpy as np
import re

df_raw = pd.read_csv('reduced_RAW_recipes.csv')
cols = ['name','minutes','n_steps','steps','description','ingredients','n_ingredients']

df_recipes = df_raw[cols]

# Create Ingredients Table
ingredients = df_recipes['ingredients']
str_ingredients = ingredients.str.cat(sep=',')
str_ingredients = str_ingredients.replace('[','')
str_ingredients = str_ingredients.replace(']','')
str_ingredients = str_ingredients.replace('\'','')
list_ingredients = str_ingredients.split(',')

print(len(list_ingredients))
df_ingredients = pd.DataFrame({'name': list_ingredients[0]}, index=[0])
for i in range(1,len(list_ingredients)):
    df_ingredients.loc[len(df_ingredients)] = list_ingredients[i]

# prepare to add list of ingredient ids
df_ingredients['id'] = str(np.arange(len(df_ingredients)))

# Create Recipes Table
df_recipes['id'] = str(np.arange(len(df_recipes)))

def get_recipes(x):
    all_recipes = df_recipes.loc[df_recipes['ingredients'].str.contains(x)]
    return all_recipes['id'].str.cat(sep=',')

def get_ingredients(x):
    all_ingredients = df_ingredients.loc[df_ingredients['recipe_ids'].str.contains(x)]
    return all_ingredients['id'].str.cat(sep=',')

combinations = []
for i in range(len(df_ingredients)):
    ingredient = df_ingredients.loc[i,'name']
    for j in range(len(df_recipes)):
        recipe = str(df_recipes.loc[j,'ingredients'])
        if ingredient in recipe:
            combinations.append([i,j])

df_junction = pd.DataFrame(combinations, columns=['ingredient_id','recipe_id'])

df_recipes.to_csv('recipes.csv', index=False)
df_ingredients.to_csv('ingredients.csv', index=False)
df_junction.to_csv('junction.csv', index=False)