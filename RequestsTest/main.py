import requests

URL = 'https://api.pokemonbattle.ru'
HEADER = {
    'Content-Type': 'application/JSON',
    'trainer_token': '6471b3d986252af7da617d9d227d849d'
}


BODYCREATED = {
    "name": "generate",
    "photo_id": -1
}


NAMECHANGES = {
    "pokemon_id": "94998",
    "name": "AvtoPokemon",
    "photo_id": -1  
}

CATCHPOKEMONS = {
    "pokemon_id": "94998"
}

response = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=BODYCREATED)
print(response.json())

response_namechanges = requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=NAMECHANGES)
print(response_namechanges.json())

response_catchpokemons = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=CATCHPOKEMONS)
print(response_catchpokemons.json())