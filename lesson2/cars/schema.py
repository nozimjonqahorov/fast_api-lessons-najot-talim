from pydantic import BaseModel
from typing import Optional


class CarCreateSchema(BaseModel):
    model:str
    desc:str


class CarOutSchema(BaseModel):
    id:int
    model : str
    decs : str


class CarUpdateSchema(BaseModel):
    model : str | None = None
    desc: str | None = None

    