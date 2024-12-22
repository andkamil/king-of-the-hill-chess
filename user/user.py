from datetime import datetime

from pydantic import BaseModel, Field

class User(BaseModel):
    nickname: str
    last_heartbeat_ts: datetime = Field(default_factory=datetime.now)

    def get_nickname(self) -> str:
        return self.nickname
    
    def set_nickname(self, nickname: str) -> None:
        self.nickname = nickname

    def get_last_heartbeat_ts(self) -> datetime:
        return self.last_heartbeat_ts
    
    def set_last_heartbeat_ts(self, timestamp: datetime) -> None:
        self.last_heartbeat_ts = timestamp
    