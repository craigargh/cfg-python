import requests

url = 'https://pokeapi.co/api/v2/pokemon/12/'

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon['name'])
