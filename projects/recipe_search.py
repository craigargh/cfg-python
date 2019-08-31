import requests


def recipe_search(ingredient):
    # https://www.food2fork.com/about/api
    api_key = ''
    result = requests.get('https://www.food2fork.com/api/search?key={}&q={}'.format(api_key, ingredient))
    data = result.json()

    return data['recipes']


def run():
    ingredient = input('Enter an ingredient: ')

    recipes = recipe_search(ingredient)

    for recipe in recipes:
        print(recipe['title'])
        print(recipe['source_url'])
        print()


run()
