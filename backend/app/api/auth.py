from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def auth_health():
    return {"message": "auth working"}
