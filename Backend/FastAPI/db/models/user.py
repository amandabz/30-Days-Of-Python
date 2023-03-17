from pydantic import BaseModel


class User(BaseModel):
    uuid: str | None
    username: str
    email: str
