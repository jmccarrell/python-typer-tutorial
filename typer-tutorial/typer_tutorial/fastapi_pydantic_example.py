from datetime import datetime
from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "KTM 500"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []

external_data = {
    "id": "23",
    "signup_ts": "2017-03-03 12:34",
    "friends": [1, "2", b"42"],
}

user = User(**external_data)
print(user)