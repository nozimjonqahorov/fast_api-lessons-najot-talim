from fastapi import APIRouter
from cars.crud import car_create, car_list, car_detail, car_delete, car_update
from cars.schema import CarCreateSchema, CarUpdateSchema
from sqlalchemy.orm import Session
from database import get_db
from fastapi import status, Depends

router  = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
def car_create_router(car:CarCreateSchema, db : Session = Depends(get_db)):
    return car_create(db, car)

@router.get('/list', status_code=status.HTTP_200_OK)
def car_list_router(db:Session = Depends(get_db)):
    return car_list(db)

@router.get('/detail/{car_id}', status_code=status.HTTP_200_OK)
def car_detail_router(car_id:int, db:Session = Depends(get_db)):
    return car_detail(db, car_id)

@router.delete('/delete/{car_id}', status_code=status.HTTP_204_NO_CONTENT)
def car_delete_router(car_id:int, db:Session = Depends(get_db)):
    return car_delete(db, car_id)

@router.patch('/update/{car_id}', status_code=status.HTTP_200_OK)
def car_update_router(car_id:int, new_data:CarUpdateSchema, db:Session = Depends(get_db)):
    return car_update(db, car_id, new_data)