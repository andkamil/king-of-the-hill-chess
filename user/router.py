from fastapi import APIRouter

from user.user_manager import user_manager

user_router = APIRouter()

@user_router.post("/user")
async def add_user(nickname: str):
    user_manager.add_user(nickname)