from fastapi import status
from fastapi.exceptions import HTTPException
from cars.models import Car
from cars.schema import CarCreateSchema, CarUpdateSchema, CarOutSchema
from sqlalchemy.orm import Session


def car_create(db:Session, car:CarCreateSchema)-> dict:
    new_car = Car(
        model = car.model,
        desc = car.desc
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return {"msg":"car created","id":new_car.id}


def car_list(db:Session) -> dict:
    cars = db.query(Car).all()
    return {
        "msg":"car list",
        "count":len(cars),
        "cars":[CarOutSchema.model_validate(c) for c in cars]
        }

def _get_car_or_404(db:Session, car_id:int)-> Car:
    car = db.query(Car).filter(Car.id == car_id).first()

    if not car:
        raise HTTPException(detail="Car not found", status_code=status.HTTP_404_NOT_FOUND)
    return car
    

def car_detail(db:Session, car_id:int)-> dict:
    car = _get_car_or_404(db, car_id)
    return  {
        "msg":"car detail",
        "car":CarOutSchema.model_validate(car)
    }

def car_delete(db:Session, car_id:Car) -> None:
    car = _get_car_or_404(db, car_id)
    db.delete(car)
    db.commit()
    return {"msg":"car deleted"}

def car_update(db:Session, car_id:Car, new_data:CarUpdateSchema) -> dict:
    car = _get_car_or_404(db, car_id)
    if new_data.model is not None:
        car.model = new_data.model  
    if new_data.desc is not None:
        car.desc = new_data.desc

    db.commit()
    db.refresh(car)

    return {
        "msg":"car updated",
        "car":CarOutSchema.model_validate(car)
    }

     