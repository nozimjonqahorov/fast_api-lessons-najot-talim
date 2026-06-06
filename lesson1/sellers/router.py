from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def seller_app():
    return {"page":"Sellers"}


@router.get('/list')
def seller_app():
    return {"selllers":["Jasur", "Inom", "Islom", "Asad"]}