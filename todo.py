from fastapi import APIRouter,Path,Request
from model import Todo
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


todo_list:Todo = []

todo = APIRouter()
templates = Jinja2Templates(directory="templates/")

@todo.get("/uaa")
def home(request:Request):
    return templates.TemplateResponse("todo.html",{"request":request})

@todo.post("/todo")
async def add_todo(request:Request):
    todo = await request.form()
    todo_list.append(todo)
    return RedirectResponse("/todo", 303)
    #{"message":"Added"}


@todo.get("/todo")
def show_todos(request:Request):
    return templates.TemplateResponse("todo.html", {"request":request,"todos":todo_list})


@todo.get("/todo/{todo_id}")
def show_one_todo(todo_id:int=Path(...,title="ID")):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"message":"ID doesn't exist"}

@todo.delete("/todo/{todo_id}")
def delete_one(todo_id:int=Path(...)):
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == todo_id:
            todo_list.pop(i)
            return {"message":"Deleted done"}
    return {"message":"Id doesn't exist"}