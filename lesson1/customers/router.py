from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def customer_app():
    return {"page":"Customers"}


@router.get('/list')
def customer_list():
    return {"customers":["Qo'qon", "Samarqand", "Tashkent", "Farg'ona"]}