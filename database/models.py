import datetime
import enum
from pydantic import BaseModel, Field


class NotificationKey(str, enum.Enum):
    registration = "registration"
    new_message = "new_message"
    new_post = "new_post"
    new_login = "new_login"


class Notification(BaseModel):
    user_id: str = Field(...)
    target_id: str = Field(default='')
    key: NotificationKey = Field(...)
    data: dict = Field(default={})
    timestamp: int = Field(default=int(datetime.datetime.now().timestamp()),
                           init_var=True)
    is_new: bool = Field(default=True, init_var=True)

    class Config:
        json_schema_extra = {
            "_id": "string",
            "user_id": "string",
            "target_id": "",
            "key": "registration",
            "data": {},
            "timestamp": 16000000,
            "is_new": True
        }
