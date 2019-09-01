# Project Brief: Search

In this project you'll create a program to search for recipes based on an ingredient. The standard project uses the Food2Fork API, but can be changed to use a different API after completing the required tasks.

You will not need any additional knowledge beyond what is covered in this course to complete this project.

## Required Tasks

These are the required tasks for this project. You sould aim to complete these tasks before adding your own ideas to the project.

- Read the Food2Fork API documentation `https://www.food2fork.com/about/api`
- Ask the user to enter an ingredient that they want to search for
- Create a function that makes a request to the Food2Fork API with the required ingredient as part of the search query
- Get the returned recipes from the API response
- Display the recipes for each search result

## Ideas for Extending the Project

Here are a few ideas for extending the project beyond the required tasks. These ideas are just suggestions, feel free to come up with your own ideas and extend the program however you want.

- Save the results to a file
- Filter the recipes based on rating
- Ask the user additional questions to decide which recipe they should choose
- Use a different searchable API (suggestions in useful resources)

## Useful Resources

API for Anime and Manga 
- Homepage `jikan.moe/`
- Documentation`jikan.docs.apiary.io`
- Example search: `https://api.jikan.moe/v3/search/anime?q=Sailor%20Moon`

Spotify API (can be very difficult to use as it requires a much more complicated setup process)
- Official Documentation `https://developer.spotify.com/documentation/web-api/`
- Python library for Spotify API `https://spotipy.readthedocs.io/en/latest/`

Twitter API (can be very difficult to use as it require a more complicated setup process)
- Official Documentation `https://developer.twitter.com/en/docs.html`
- Python library for Twitter API `http://docs.tweepy.org/en/v3.5.0/api.html`

## Example Project Code

In this section you will find some example code to complete the required tasks. You can use this code for guidance if you are finding it difficult to complete the required tasks for this project. 

```python 
import requests


def recipe_search(ingredient):
    # Register to get an API key https://www.food2fork.com/about/api
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
```