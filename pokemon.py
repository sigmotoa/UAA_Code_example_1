from fastapi import APIRouter, Path, Request
from model import Pokemon
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pokemon_api import all_pokemon, pokemon_details
from fastapi.staticfiles import StaticFiles
import os


pokemon = APIRouter()

templates = Jinja2Templates(directory = "templates/")

pokemon.mount("/static",StaticFiles(directory="static/"),name="static")

@pokemon.get("/pokemon")
def show_all_pokemon(request:Request):
    return templates.TemplateResponse("home.html",{"request":request, "title":"pokemon sigmotoa","text":"Mis pokemones", "images":os.listdir("static")})
    #return all_pokemon()

@pokemon.get("/pokemon2")
def show_pokemon_detail(request:Request):
    pokemons = pokemon_details()
    print(pokemons)
    return templates.TemplateResponse("pokemon.html",{"request":request, "title":"pokemon sigmotoa","text":"Un texto muy extenso", "pokemons":pokemons})
    #(pokemon_details())

@pokemon.get("/detail")
def show_detail_pokemon(request:Request):
    pokemons = pokemon_details()
    return templates.TemplateResponse("elementos.html", {"request":request, "title":"Pokemon Detail", "pokemons":pokemons})