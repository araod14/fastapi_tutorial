#path
from fastapi import APIRouter
from schemas.person import Person, PersonOut
from fastapi import status
from fastapi import Body , Query , Path, Form
from typing import Optional

from config.db import conn
from models.person import persons
from schemas.person import Person

person = APIRouter()

@person.get(
    path="/",
    status_code = status.HTTP_200_OK
    )
def home():
    return {"Epale": "QLQX"}

#Request and response body
@person.post(
    path = "/person/new", 
    response_model = PersonOut,
    status_code = status.HTTP_201_CREATED
    )
def create_person(person: Person = Body(...)):
    new_person = {'first_name':person.first_name, 'last_name':person.last_name, 'age':person.age, 'hair_color':person.hair_color}
    result = conn.execute(persons.insert().values(new_person))
    return conn.execute(persons.select().where(persons.c.id==result.inserted_primary_key['id'])).first()


# Validations: query parameters
@person.get(
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
    age: str = Query(
        ...,
        title = "Person age",
        description = "This is the person age. It's required"
    )
    ):
    return conn.execute(persons.select().where(persons.c.age == age)).first()

@person.get(
    path = "/person/detail",
    status_code = status.HTTP_200_OK
    )
def show_person(
    id:int = Query(
        ..., 
        gt=0,
        title = "Person ID ",
        description = "This is the person ID. it's required and its grather than 0")
    ):
    return conn.execute(persons.select().where(persons.c.id == id)).first()

@person.delete(
    path = "/person/detail",
    status_code = status.HTTP_200_OK
    )
def delete_person(
    id:int = Query(
        ..., 
        gt=0,
        title = "Person ID ",
        description = "This is the person ID. it's required and its grather than 0")
    ):
    conn.execute(persons.delete().where(persons.c.id == id))
    return 'deleted'

@person.put(
    path = "/person/detail",
    status_code = status.HTTP_201_CREATED
    )
def update_person(
    id: str, 
    person: Person
    ):
    conn.execute(persons.update().values(first_name = person.first_name, 
                last_name= person.last_name, age=person.age ).where(persons.c.id == id))
    return conn.execute(persons.select().where(persons.c.id == id)).first()