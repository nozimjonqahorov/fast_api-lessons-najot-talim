from fastapi import FastAPI
import cars.models
from database import engine


app = FastAPI()

cars.models.Base.metadata.create_all(bind = engine)

@app.get('/')
def index():
    return {"msg":"Main home"}