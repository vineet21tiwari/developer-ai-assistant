from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def chat_health():
    return {"message": "chat working"}
