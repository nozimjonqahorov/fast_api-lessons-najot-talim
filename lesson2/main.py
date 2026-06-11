from fastapi import FastAPI
from cars.router import router as car_router

app = FastAPI()

app.include_router(car_router, prefix='/car', tags=['car'])


@app.get('/')
def index():
    return {"msg":"Main home"}