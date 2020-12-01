import requests
import urllib3.request
import re

# TODO
# Different recipes and their Regular expressions to find the ingredients and title
#################### DK-Kogebogen ##################################
# https://www.dk-kogebogen.dk/opskrifter/5372/spaghetti-carbonara
# titel
# <span itemprop="name"><h1><center>(.*?)</center></H1></span>
# ingredienser
# <span class="hidden" itemprop="recipeIngredient">(.*?)</span>
####################################################################
###################     Meny     ###################################
# https://meny.dk/node/4518
# titel
# <h1 class="title">(.*?)</h1>
# ingredienser
# <div class="spice-4">(.*?)</div>
####################################################################
# Need a loop to iterate through different website (recipes)

for i in range(4400, 4410):
    url ="https://meny.dk/node/" + str(i)
    r = requests.get(url)



#url = "https://www.dk-kogebogen.dk/opskrifter/5372/spaghetti-carbonara"


source = r.text
dict = {"æ": "\xc3\xa6", "ø": "\xc3\xb8", "å": "\xc3\xa5"}

# print(r.content)

# Prototype for the ingredient dictionary
# ingredient = {'amount', 'unit', 'name'}
# This will hold all the ingredients
ingredients = []
# Prototype for recipe
# Recipe = {'name', 'ingredients', 'url', 'people'}
# Holds all the recipes
Recipes = []

pattern_title = '<span itemprop="name"><h1><center>(.*?)</center></H1></span>'
pattern_ingredients = '<span class="hidden" itemprop="recipeIngredient">(.*?)</span>'

# Finds the title via Regular expression
matches_title = re.findall(pattern_title, source)
# print(matches_title)

# Finds the ingredients via Regular expression
matches_ingredients = re.findall(pattern_ingredients, source)

# fills the ingredients list up by iterating trough the matches
for element in matches_ingredients:
    new_ingredient = {}
    substring = element.split()
    # print(element)
    if(len(substring) == 1):
        new_ingredient['amount'] = 0
        new_ingredient['unit'] = ""
        new_ingredient['name'] = substring[0]

    if(len(substring) == 2):
        new_ingredient['amount'] = substring[0]
        new_ingredient['unit'] = ""
        new_ingredient['name'] = substring[1]

    if(len(substring) > 2):
        new_ingredient['amount'] = substring[0]
        new_ingredient['unit'] = substring[1]
        new_ingredient['name'] = (" ".join(substring[2:]))

    if(len(substring) < 1):
        print("Error: Ingredient substring less than 1")

    ingredients.append(new_ingredient)
    # print(sub)

# print(ingredients)
new_recipe = {'name': matches_title, 'ingredients': ingredients, 'url': r.url, 'people': 4}
# print(new_recipe)
Recipes.append(new_recipe)


for element in Recipes:
    print(element['name'])


# The amount of people this meal would be served for

# What things i need to search for in the HTML

# <span itemprop="name"><h1><center> Spaghetti Carbonara</center></H1></span>
# <span class="hidden" itemprop="recipeIngredient">125 gram Bacon i skiver </span>
# <span class="hidden" itemprop="recipeIngredient">500 gram Spaghetti, t\xc3\xb8rret</span>
# <span class="hidden" itemprop="recipeIngredient">4  \xc3\x86g</span>
# <span class="hidden" itemprop="recipeIngredient">100 gram Parmesanost. revet</span>
# <span class="hidden" itemprop="recipeIngredient">3 dl. Piskefl\xc3\xb8de</span>
# <span class="hidden" itemprop="recipeIngredient">  Salt</span>
# <span class="hidden" itemprop="recipeIngredient">  Peber</span>

# print(r.content)
