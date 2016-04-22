#!/usr/bin/env python3

import bs4, json, pickle, requests, shutil, signal, sys, time, slugify


class Cocktail_(object):
    def __init__(self, name, glass=None, ingredients=None, recipe=None, image=None):
        self.name = name

    def __str__(self):
        result = 'Name: {0}, '.format(self.name)
        result += 'Glass: {0}, '.format(self.glass)
        result += 'Ingredients: {0}, '.format(self.ingredients)
        result += 'Recipe: {0}'.format(self.recipe)
        return result


# TODO: figure out how to align well automatically
# TODO: also need to keep this updated
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
        print('Getting data for {0} cocktails'.format(len(cocktail_list)))
        numCocktails = 0

        # Running list of cocktails parsed
        cocktails = []

        for cocktail in cocktail_list:
            # Create the object
            c = Cocktail_(cocktail['strDrink'])

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

            # Extract the type of glass and recipe
            c.glass = dictionary['strGlass']
            c.recipe = dictionary['strInstructions']

            # Get an image for the cocktail
            c.image = get_image(c.name, 'cocktails', 'cocktail')

            # Add the cocktail to the list
            cocktails.append(c)
            numCocktails += 1
            print('{0}: {1}'.format(numCocktails, c.name))
            # time.sleep(1)   # Throttle the downloads

        return cocktails


# ------------------------------------------------------------------------------
# IMAGES
# ------------------------------------------------------------------------------


def run_cocktail_images():
    print('Getting images for cocktails')
    with open('cocktails.pkl', 'rb') as f:
        cocktails = pickle.load(f)
        for c in cocktails:
            path = get_image(c.name, 'cocktails', 'cocktail')
            c.image = path
            print(c.name)
            # time.sleep(1)


def run_ingredient_images():
    # Get the images for the ingredients
    print('Getting images for ingredients')
    with open('cocktails.pkl', 'rb') as f:
        cocktails = pickle.load(f)
        ingredients_found = set()
        for c in cocktails:
            for i, _ in c.ingredients:  # _ for the amount of the ingredient
                if i not in ingredients_found:
                    get_image(i, 'ingredients')
                    ingredients_found.add(i)
                    print(i)
                    # time.sleep(1)


def get_image(name, directory, append=''):
    # Replace characters to make a searchable string
    # name = name.replace(' ', '+')
    # name = name.replace('/', '\\')  # TODO: Probably not the best idea, works for now
    name = slugify.slugify(name)

    # Get the html from Google images
    url = 'https://www.google.com/search?safe=on&tbm=isch&q={0}+{1}'.format(name, append)
    res = requests.get(url)

    # Get the first image
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    img_url = soup.find('img')['src']
    res = requests.get(img_url, stream=True)

    # Just save as jpg, because meh
    # Also leaving the plusses in (also because meh)
    with open('./static/images/{0}/{1}.jpg'.format(directory, name), 'wb') as f:
        shutil.copyfileobj(res.raw, f)

    return '{0}/{1}'.format(directory, name)


# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------


def main():
    # Catch ctrl-c
    signal.signal(signal.SIGINT, lambda _, __: sys.exit(0))

    # If no options passed in, run the entire program
    if len(sys.argv) == 1:
        run_init()
        run_cocktail_images()
        run_ingredient_images()

    # Get the initial data
    elif sys.argv[1] == '--init' or sys.argv[1] == '-i':
        run_init()

    # Get images for cocktails and ingredients
    elif sys.argv[1] == '--images':
        run_cocktail_images()
        run_ingredient_images()

    elif sys.argv[1] == '--cocktailimages' or sys.argv[1] == '-c':
        run_cocktail_images()

    elif sys.argv[1] == '--ingredientimages' or sys.argv[1] == '-n':
        run_ingredient_images()

    # Print usage
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print_usage()

    # Print usage
    else:
        print('Unknown command {0}'.format(sys.argv[1]))
        print_usage()


if __name__ == '__main__':
    main()
