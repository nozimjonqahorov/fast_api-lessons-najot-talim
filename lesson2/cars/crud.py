from fastapi import status
from fastapi.exceptions import HTTPException
from cars.models import Car
from cars.schema import CarCreateSchema, CarUpdateSchema
from sqlalchemy.orm import Session


def car_create(db:Session, car:CarCreateSchema):
    new_car = Car(
        model = car.model,
        desc = car.desc
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    response = {
        "msg":"car created",
        "status":status.HTTP_201_CREATED,
        "id":new_car.id

    }

    return response


def car_list(db:Session):
    cars = db.query(Car).all()
    
    response = {
        "msg":"car list",
        "status":status.HTTP_200_OK,
        "count":len(cars),
        "cars":cars

    }

    return response



def car_detail(db:Session, car_id:Car):
    car = db.query(Car).filter(Car.id == car_id).first()

    if not car:
        raise HTTPException(detail="Car not found", status_code=status.HTTP_404_NOT_FOUND)
    
    response = {
        "msg":"car detail",
        "status":status.HTTP_200_OK,
        "car":car

    }

    return response


def car_delete(db:Session, car_id:Car):
    car = db.query(Car).filter(Car.id == car_id).first()

    if not car:
        raise HTTPException(detail="Car not found", status_code=status.HTTP_404_NOT_FOUND)
    
    db.delete(car)
    db.commit()

    response = {
        "msg":"car deleted",
        "status":status.HTTP_204_NO_CONTENT,
    }

    return response

def car_update(db:Session, car_id:Car, new_data:CarUpdateSchema):
    car = db.query(Car).filter(Car.id == car_id).first()

    if not car:
        raise HTTPException(detail="Car not found", status_code=status.HTTP_404_NOT_FOUND)
    
    new_model = new_data.get("model", "")
    new_desc = new_data.get("desc", "")
    
    if new_model:
        car.model = new_model

    if new_desc:
        car.desc = new_desc

    db.commit()
    db.refresh(car)

    response = {
        "msg":"car updated",
        "status":status.HTTP_200_OK,
        "car":car
    }

    return response