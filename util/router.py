from fastapi import APIRouter

from storage.storage import storage

heartbeat_router = APIRouter()

@heartbeat_router.post("/heartbeat")
async def update_user_heartbeat_ts(nickname: str):
    storage.update_user_heartbeat_ts(nickname)