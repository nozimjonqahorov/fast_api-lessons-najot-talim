from pydantic import BaseModel



class CarCreate(BaseModel):
    model:str
    desc:str