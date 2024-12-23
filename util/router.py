from fastapi import APIRouter

from user.user_manager import user_manager

heartbeat_router = APIRouter()

@heartbeat_router.post("/heartbeat")
async def update_user_heartbeat_ts(nickname: str):
    user_manager.update_user_heartbeat_ts(nickname)