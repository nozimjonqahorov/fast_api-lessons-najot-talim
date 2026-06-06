from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def product_app():
    return {"page":"Products"}


@router.get('/list')
def product_app():
    return {"products":["Olma", "Anor", "Anjir", "Gelos"]}