**Starter:** ???

---

![Code First: Girls](images/logo_large.png)

#### Python Session 5

---

This session
1. Files
1. Pip package manager
1. APIs

---

### Python Pip

----

**pip:** A package manager used to install libraries that other people have written

----

pip is used via the terminal (command-line)

![Opening the terminal](gifs/terminal.gif)

----

Install the `requests` library using pip

``` command-line
pip install requests
```

---

### APIs: Reading Stuff

----

**Application Programming Interface (API):** A way to send data between programs

Web APIs allow you to do this over the internet.

----

Pokéapi is an API to get data about Pokémon

[pokeapi.co/](https://pokeapi.co/)

----

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls

[https://pokeapi.co/api/v2/pokemon/6/](https://pokeapi.co/api/v2/pokemon/6/)

----


Save this as `get_pokemon.py`

```python
import requests
from pprint import pprint

url = 'https://pokeapi.co/api/v2/pokemon/151/'

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon)
```

----

Reponse status codes:

Status Code | Name | Explanation
--- | --- | ---
200 | OK | The request worked
404 | Not found | Couldn't find the url you requested
400 | Bad request | The request you made isn't understood


----

**Task:** Get the *height* and *weight* of the Pokemon and print the output

Add `input()` to choose which Pokemon you want information about

----

Solution

```python
import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])
```

---


### Recap

----

This session
1. Files
1. Pip package manager
1. APIs

----

**Homework:** Session 5 homework questions in your student guide

Look at the project suggestions in your student guide and think about which one you might like to work on
