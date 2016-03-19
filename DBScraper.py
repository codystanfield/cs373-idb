#!/usr/bin/env python3

import json, pickle, requests, signal, sys, time


class Cocktail(object):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        result = 'Name: {0}, '.format(self.name)
        result += 'Glass: {0}, '.format(self.glass)
        result += 'Ingredients: {0}, '.format(self.ingredients)
        result += 'Recipe: {0}'.format(self.recipe)
        return result


# TODO: figure out how to align well automatically
def print_usage():
    print('usage:\n'
          '--init\t\tget the initial data from The Cocktail Database\n'
          '-h or --help\tprint this message')
        
        
# ------------------------------------------------------------------------------
# INIT
# ------------------------------------------------------------------------------


def run_init():
    print('Running init')
    cocktail_list = get_list_of_cocktails()
    cocktails = get_all_cocktails(cocktail_list)

    # Output to pickle file
    with open('cocktails.pkl', 'wb') as output:
        pickle.dump(cocktails, output, pickle.HIGHEST_PROTOCOL)


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
                if ingredient == '' or ingredient is None:
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
            print('{0}: {1}'.format(numCocktails, c.name))
            time.sleep(5)   # Throttle the downloads
            
        return cocktails
    

# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------

    
def main():
    # Catch ctrl-c
    signal.signal(signal.SIGINT, lambda _, __: sys.exit(0))
    
    # If no options passed in, run the entire program
    if len(sys.argv) == 1:
        run_init()

    # If getting the initial data
    elif sys.argv[1] == '--init':
        run_init()
    
    # Print usage
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_usage()
        
    # Print usage
    else:
        print('Unknown command {0}'.format(sys.argv[1]))
        print_usage()
        
        
if __name__ == '__main__':
    main()
