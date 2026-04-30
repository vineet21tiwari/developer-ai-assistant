from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def code_assistant_health():
    return {"message": "code_assistant working"}
