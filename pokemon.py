from fastapi import APIRouter, Path, Request
from model import Pokemon
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pokemon_api import all_pokemon, pokemon_details


pokemon = APIRouter()

templates = Jinja2Templates(directory = "templates/")



@pokemon.get("/pokemon")
def show_all_pokemon():

    return all_pokemon()

@pokemon.get("/pokemon2")
def show_pokemon_detail():


    return(pokemon_details())