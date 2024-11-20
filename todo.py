from fastapi import APIRouter
from model import Todo

todo_list:Todo = []

todo = APIRouter()

@todo.post("/todo")
def add_todo(todo:Todo):
    todo_list.append(todo)
    return {"message":"Added"}


@todo.get("/todo")
def show_todos():
    return {"todos":todo_list}