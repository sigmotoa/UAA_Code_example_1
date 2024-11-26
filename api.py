from fastapi import FastAPI
from todo import todo
from pokemon import pokemon
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static",StaticFiles(directory="static/"),name="static")

@app.get("/")
def home():
    return "Bienvenidos"


@app.get("/name/{name}")
def greeting(name:str):
    return "Hello "+name

app.include_router(todo)
app.include_router(pokemon)