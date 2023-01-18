#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Body , Query , Path, Form


app = FastAPI()

class HairColor(Enum):
    white = "White"
    gray = "Gray"
    brown = "Brown"
    blonde = "Blonde"

class Location(BaseModel):
    city: str
    state: str
    country: str

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=0,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=0,
        max_length=50
    )
    age: int = Field(
        ...,
        gt = 0,
        le = 50
    )
    hair_color: Optional[HairColor] = Field(default = None)
    is_married: Optional[bool] = Field(default = None)

class PersonOut(PersonBase):
    pass

class Person(PersonBase):
    password: str = Field(
        ...,
        min_length= 8
    )
    
class LoginOut(BaseModel):
    username: str = Field(...,max_length=20, example="miguel2021")
    message: str = Field(default="Loginsucccesfully")

@app.get(
    path="/",
    status_code = status.HTTP_200_OK
    )
def home():
    return {"Epale": "QLQX"}

#Request and response body
@app.post(
    path = "/person/new", 
    response_model = PersonOut,
    status_code = status.HTTP_201_CREATED
    )
def create_person(person: Person = Body(...)):
    return person

# Validations: query parameters
@app.get(
    path = "/person/detail",
    status_code = status.HTTP_200_OK
    )
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1, 
        max_length=50,
        title = "Person name ",
        description = "This is the person name. It's between 1 and 50 charapter"
    ),
    age: int = Query(
        ...,
        title = "Person age",
        description = "This is the person age. It's required"
    )
    ):
    return {name: age}

@app.get(
    path = "/person/detail/{person_id}",
    status_code = status.HTTP_200_OK
    )
def show_person(
    person_id:int = Path(
        ..., 
        gt=0,
        title = "Person ID ",
        description = "This is the person ID. it's required and its grather than 0")
    ):
    return {person_id: "it exists!"}

@app.put(
    path = "/person/{person_id}",
    status_code = status.HTTP_202_ACCEPTED
    )
def update_person(
    person_id: int = Path(
        ...,
        title = "Person ID",
        description = "This is the person ID",
        gt = 0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
    ):
    results = person.dict()
    results.update(location.dict())
    return results

@app.post(
    path = "/login",
    response_model = LoginOut,
    status_code = status.HTTP_200_OK
    )
def login():
    pass