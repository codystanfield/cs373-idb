#!/usr/bin/env python3

import json, requests


class Cocktail(object):    
    def __init__(self, name):
        self.name = name
        
    
    def __str__(self):
        result = 'Name: {0}, '.format(self.name)
        result += 'Glass: {0}, '.format(self.glass)
        result += 'Ingredients: {0}, '.format(self.ingredients)
        result += 'Recipe: {0}'.format(self.recipe)
        return result
        
        
def get_list_of_cocktails():
    """Get the list of cocktails from The Cocktail DB"""
    
    res = requests.get('http://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error downloading page: {0}'.format(exc))
    
    return json.loads(res.text)['drinks']
    
    
def get_all_cocktails(cocktail_list):
        print('Getting the data for {0} cocktails'.format(len(cocktail_list)))
        numCocktails = 0
        
        # Running list of cocktails parsed
        cocktails = []
        
        for cocktail in cocktail_list:
            # Create the object
            c = Cocktail(cocktail['strDrink'])
            
            # Request the json
            res = requests.get('http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}'.format(cocktail['idDrink']))
            try:
                res.raise_for_status()
            except Exception as exc:
                print('Error downloading page: {0}'.format(exc))
                
            # Parse the json into a dicitonary
            dictionary = json.loads(res.text)['drinks'][0]

            # Extract the ingredients
            ingredients = []
            for i in range(1, 15):
                ingredient = dictionary['strIngredient{0}'.format(i)]
                if ingredient == '':
                    break
                ingredients.append((ingredient, dictionary['strMeasure{0}'.format(i)]))
            c.ingredients = ingredients
            
            # Extract the image
            # TODO
            
            # Extract the type of glass and recipe
            c.glass = dictionary['strGlass']
            c.recipe = dictionary['strInstructions']
            
            # Add the cocktail to the list
            cocktails.append(c)
            numCocktails += 1
            print(numCocktails)
            
            # TODO: should really throttle this
        
        return cocktails
    
    
def main():
    cocktail_list = get_list_of_cocktails()
    cocktails = get_all_cocktails(cocktail_list)
        
        
if __name__ == '__main__':
    main()
