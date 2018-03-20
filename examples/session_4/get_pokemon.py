import requests

url = 'https://pokeapi.co/api/v2/pokemon/98/'

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon['name'])
