from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def order_app():
    return {"page":"Orders"}


@router.get('/list')
def order_app():
    return {"orders":["dhfkj32443", "324ror", "jfwel43435", "2wkfwekwe23"]}