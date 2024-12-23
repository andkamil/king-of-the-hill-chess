from pydantic import BaseModel

from user.user import User

from datetime import datetime

class Storage(BaseModel):
    # games: list[Game] | None = None
    users: dict[str, User] | None = None

    def add_user(self, nickname: str) -> None:
        if nickname in self.users:
            return False
        user = User(nickname=nickname)
        self.users[nickname] = nickname

    def remove_user(self, nickname: str) -> None:
        if nickname not in self.users:
            return False
        del self.users[nickname]

    def update_user_heartbeat_ts(self, nickname: str) -> None:
        if nickname not in self.users:
            return False
        self.users[nickname].set_last_heartbeat_ts(datetime.now())

storage = Storage()

