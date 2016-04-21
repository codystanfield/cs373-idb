#! /usr/bin/env python3

from models import Amount, Cocktail, Ingredient
import pickle

cocktail_idx = {}
ingredient_idx = {}

# Loop through Cocktails
for c in Cocktail.query.all():
    # Name
    for word in c.name.split(' '):
        if word not in cocktail_idx:
            cocktail_idx[word] = set()
        cocktail_idx[word].add(c.id_)
    
    # Glass
    for word in c.glass.split(' '):
        if word not in cocktail_idx:
            cocktail_idx[word] = set()
        cocktail_idx[word].add(c.id_)
    
    # Recipe
    for word in c.recipe:
        if word not in cocktail_idx:
            cocktail_idx[word] = set()
        cocktail_idx[word].add(c.id_)
    
    for i in Amount.query.filter(Amount.cocktail == c.id_):
        ing = Ingredient.query.filter(Ingredient.id_ == i.ingredient).one_or_none()
        for word in ing.name.split(' '):
            if word not in cocktail_idx:
                cocktail_idx[word] = set()
            cocktail_idx[word].add(c.id_)

with open('cocktail_idx.pkl', 'wb') as output:
    pickle.dump(cocktail_idx, output, pickle.HIGHEST_PROTOCOL)

        
# print(cocktail_idx)


for i in Ingredient.query.all():
    # Name
    for word in i.name.split(' '):
        if word not in ingredient_idx:
            ingredient_idx[word] = set()
        ingredient_idx[word].add(i.id_)
    
    # Cocktails
    for a in Amount.query.filter(Amount.ingredient == i.id_):
        c = Cocktail.query.filter(Cocktail.id_ == a.cocktail).one_or_none()
        for word in c.name.split(' '):
            if word not in ingredient_idx:
                ingredient_idx[word] = set()
            ingredient_idx[word].add(i.id_)
        
    # Number of Cocktails
    num = Amount.query.filter(Amount.ingredient == i.id_).count()
    if num not in ingredient_idx:
        ingredient_idx[num] = set()
    ingredient_idx[num].add(i.id_)

with open('ingredient_idx.pkl', 'wb') as output:
    pickle.dump(ingredient_idx, output, pickle.HIGHEST_PROTOCOL)
    
# print(ingredient_idx)
