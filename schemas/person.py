#class

from enum import Enum
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import Field

"""class HairColor(Enum):
    white = "White"
    gray = "Gray"
    brown = "Brown"
    blonde = "Blonde"

class Location(BaseModel):
    city: str
    state: str
    country: str
"""
class PersonBase(BaseModel):
    id: Optional[str]
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

#    hair_color: Optional[HairColor] = Field(default = None)
#    is_married: Optional[bool] = Field(default = None)

class PersonOut(PersonBase):
    pass

class Person(PersonBase):
    pass
    """
    password: str = Field(
        ...,
        min_length= 8
    )
    """
class LoginOut(BaseModel):
    username: str = Field(...,max_length=20, example="miguel2021")
    message: str = Field(default="Loginsucccesfully")
