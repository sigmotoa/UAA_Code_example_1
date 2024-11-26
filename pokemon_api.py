import requests
import json
from typing import List, Dict
from model import Pokemon

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

list_pokemon:List[str]=[]
list_total=[]

def all_pokemon():
    
    response = requests.get(BASE_URL)
    if response.status_code==200:
        data = response.json()
        list_pokemon.extend([char["name"] for char in data.get("results", [])])
        return data.get("results",[])
        
        
    else:
        return{"message":response.status_code}


def pokemon_details():
    if not list_pokemon:
        all_pokemon()

    for pokemon in list_pokemon:
        petition=f"{BASE_URL}/{pokemon}"
        response = requests.get(petition)
        pokemon_data = response.json()
        list_total.append(Pokemon(id=pokemon_data["id"],name=pokemon_data["name"],
        img=pokemon_data["sprites"]["other"]["dream_world"]["front_default"]))

    return (list_total)        