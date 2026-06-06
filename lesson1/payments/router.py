from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def payment_app():
    return {"page":"Payments"}


@router.get('/list')
def payment_list():
    return {"payments":["Karta", "Naxt", "Umsiz", "Bank Transfer"]}