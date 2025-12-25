#connecting API using python 
import requests as rq

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
  url = f"{base_url}/pokemon/{name}"
  response = rq.get(url)
  if response.status_code == 200:
    # print("data retrieved successfully...")
    pokemon_data = response.json()
    # print(pokemon_data)
    return pokemon_data
  else:
    print(f"failed to retrieve data {response.status_code} ")
  print(response.status_code)

pokemon_name = input("Enter a pokemon name: ").strip()
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info:
  print(f"Name: {pokemon_info["name"].title()}")
  print(f"Id: {pokemon_info["id"]}")
  print(f"Height: {pokemon_info["height"]}")
  print(f"Weight: {pokemon_info["weight"]}")