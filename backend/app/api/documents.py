from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def documents_health():
    return {"message": "documents working"}
