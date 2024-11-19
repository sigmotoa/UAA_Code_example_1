from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Bienvenidos"


@app.get("/name/{name}")
def greeting(name:str):
    return "Hello "+name