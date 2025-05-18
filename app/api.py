from fastapi import APIRouter


router = APIRouter()


@router.get(path="/hello")
async def root():
    return {"message": "Hello World"}
