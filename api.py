from fastapi import FastAPI
from todo import todo
from pokemon import pokemon

app = FastAPI()

@app.get("/")
def home():
    return "Bienvenidos"


@app.get("/name/{name}")
def greeting(name:str):
    return "Hello "+name

app.include_router(todo)
app.include_router(pokemon)