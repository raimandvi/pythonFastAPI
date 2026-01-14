from fastapi import FastAPI


app = FastAPI()
@app.get("/")
def home():
    return {"message": "FastAPI is working"}


@app.get("/add")
def add_num(a: int, b:int):
    return {"result": a + b}

# Request Body (Pydantic Model)

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    marks: float

@app.post("/student")
def create_student(student: Student):
    return student
