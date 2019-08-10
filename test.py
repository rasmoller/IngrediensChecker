import requests
import re

# Holds all the ingredients which are dictonaries
ingredients = []
# Holds the ingredients (the above variable), the name and the URL for the recipe
Recipes = []


def getRecipe(str):
    r = requests.get(url)

    source = r.text

    pattern_title = '<h1 class="title">(.*?)</h1>'
    pattern_ingredients = '<div class="spice-[0-9]">(.*)</div>'

    matches_title = re.findall(pattern_title, source)
    matches_ingredients = re.findall(pattern_ingredients, source)

    if(len(matches_title) < 1):
        return 1
    elif(len(matches_ingredients) < 1):
        return 2
    else:
        ingredients = matches_ingredients[0].split("<br />")

        new_recipe = {'name': matches_title,
            'ingredients': ingredients, 'url': r.url}
        return new_recipe


for i in range(4518, 4550): # 4550
    url = "https://meny.dk/node/" + str(i)
    R = getRecipe(url)
    if(R == 1):
        print("Error getting recipe number %i", i)
    elif(R == 2):
        print("Ingredients list is non existent at recipe number: %i", i)
    else:
        Recipes.append(R)


for rec in Recipes:
    print()
    print(rec["name"])
    print(rec["ingredients"])
#pattern_title = '<span itemprop="name"><h1><center>(.*)</center></H1></span>'

#matches_title = re.findall(pattern_title, source)

# titel
# <h1 class="title">(.*?)</h1>
# ingredienser
# <div class="spice-[0-9]">(.*?)</div>