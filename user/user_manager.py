from pydantic import BaseModel

from user.user import User

from datetime import datetime

class UserManager(BaseModel):
    users: dict[str, User] = {}

    def add_user(self, nickname: str) -> None:
        if nickname in self.users:
            return False
        user = User(nickname=nickname)
        self.users[nickname] = user
        print(self.users)

    def remove_user(self, nickname: str) -> None:
        if nickname not in self.users:
            return False
        del self.users[nickname]

    def update_user_heartbeat_ts(self, nickname: str) -> None:
        if nickname not in self.users:
            return False
        self.users[nickname].set_last_heartbeat_ts(datetime.now())

user_manager = UserManager()

