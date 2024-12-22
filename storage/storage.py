from pydantic import BaseModel

from user.user import User

class Storage(BaseModel):
    # games: list[Game] | None = None
    users: list[User] | None = None