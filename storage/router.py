from fastapi import APIRouter

from storage.storage import storage

user_router = APIRouter()

@user_router.post("/user")
async def add_user(nickname: str):
    storage.add_user(nickname)