from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def quiz_health():
    return {"message": "quiz working"}
