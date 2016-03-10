#!/usr/bin/env python3

import json, requests


class Cocktail(object):
    def __init__(self, name, ingredients, recipe):
        """Initialize
        
        name: str
        ingredients: dict of name to amount TODO: order the dict
        recipe: String instructions TODO: could be list of instructions instead
        """
        
        self.name = name
        self.ingredients = ingredients
        self.recipe = recipe
        
        
def get_list_of_cocktails():
    """Get the list of cocktails from The Cocktail DB"""
    
    res = requests.get('http://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error downloading page: {0}'.format(exc))
    
    return json.loads(res.text)['drinks']
    
    
def main():
    cocktails = get_list_of_cocktails()
        
        
if __name__ == '__main__':
    main()
