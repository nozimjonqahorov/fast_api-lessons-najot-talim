from fastapi import status
from fastapi.exceptions import HTTPException
from models import Car
from schema import CarCreate
from sqlalchemy.orm import Session


def car_list(db:Session, car: CarCreate):
    cars = db.query(Car).all()
    return cars
