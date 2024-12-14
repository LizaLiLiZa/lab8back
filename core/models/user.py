# pylint: disable=E0213
import re
from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException

class UserModel(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value: str):
        pattern = r"^[a-zA-Zа-яА-Я0-9,./*-_=+]{8,16}$"
        if re.match(pattern, value):
            return value
        raise HTTPException(status_code=422, detail="Неверный формат пароля")
