from pydantic import BaseModel, ConfigDict
from typing import Optional


class CarCreateSchema(BaseModel):
    model:str
    desc:str


class CarOutSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    id:int
    model : str
    desc : str


class CarUpdateSchema(BaseModel):
    model : str | None = None
    desc: str | None = None

    