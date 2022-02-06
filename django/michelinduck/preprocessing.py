import pandas as pd
import numpy as np
import re

df_raw = pd.read_csv('reduced_RAW_recipes.csv')
cols = ['name', 'minutes', 'n_steps', 'steps',
        'description', 'ingredients', 'n_ingredients']

df_recipes = df_raw[cols]

# Create Ingredients Table
ingredients = df_recipes['ingredients']
str_ingredients = ingredients.str.cat(sep=',')
str_ingredients = str_ingredients.replace('[', '')
str_ingredients = str_ingredients.replace(']', '')
str_ingredients = str_ingredients.replace('\'', '')
list_ingredients = str_ingredients.split(',')

unique_list = set()
for x in list_ingredients:
    unique_list.add(x)

unique_list = list(unique_list)
df_ingredients = pd.DataFrame({'name': unique_list[0]}, index=[0])
for i in range(1, len(unique_list)):
    df_ingredients.loc[len(df_ingredients)] = unique_list[i]

# # prepare to add list of ingredient ids
# df_ingredients['id'] = np.arange(len(df_ingredients))

# # Create Recipes Table
# df_recipes['id'] = np.arange(len(df_recipes))

df_ingredients['id'] = 0
df_recipes['id'] = 0
combinations = []
print(df_ingredients.loc[0, 'name'])
for i in range(len(df_ingredients)):
    ingredient = df_ingredients.loc[i, 'name']
    df_ingredients.loc[i, 'id'] = i
    for j in range(len(df_recipes)):
        recipe = str(df_recipes.loc[j, 'ingredients'])
        df_recipes.loc[j, 'id'] = j
        if ingredient in recipe:
            combinations.append([i, j])
            # print(ingredient)
            # print(recipe)
            # print(i)
            # print(j)
            # break
df_junction = pd.DataFrame(combinations, columns=[
                           'ingredient_id', 'recipe_id'])


df_recipes.to_csv('recipes.csv', index=False)
df_ingredients.to_csv('ingredients.csv', index=False)
df_junction.to_csv('junction.csv', index=False)
