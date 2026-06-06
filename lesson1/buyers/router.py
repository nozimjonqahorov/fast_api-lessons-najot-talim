from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def buyer_app():
    return {"page":"Buyers"}


@router.get('/list')
def buyer_app():
    return {"buyers":["Nozim", "Mirzovali", "Anvar"]}