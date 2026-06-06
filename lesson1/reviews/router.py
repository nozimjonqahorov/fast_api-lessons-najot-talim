from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def review_app():
    return {"page":"Reviews"}


@router.get('/list')
def review_list():
    return {"reviews":["Juda yaxshi", "Yaxshi", "Arzoqladi", "Yomon", "Juda yomon"]}