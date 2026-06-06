from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def inventory_app():
    return {"page":"Inventory"}


@router.get('/list')
def inventory_list():
    return {"inventory":["Telefon", "Noutbuk", "Monitor", "Keyboard", "Mouse"]}