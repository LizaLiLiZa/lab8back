import json
from fastapi import HTTPException

from core.models.requests import UserRequest
from core.models.requests import LoginRequest

class UserService():
    def get_user(self, info: LoginRequest):
        path = "core//bd//user.json"
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for i in data:
                if i["username"] == info.username:
                    print(i["password"], info.password)
                    if i["password"] == info.password:
                        return f"Welcome, {info.username}"
                    return HTTPException(status_code=422, detail="Не верно введен пароль!")
            raise HTTPException(status_code=422, detail="Нет пользователя с таким именем!")

    def add_data(self, user: UserRequest):
        path_id = "core//bd//id.json"
        path_data = "core//bd//user.json"

        with open(path_data, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for i in data:
                if i["username"] == user.username:
                    raise HTTPException(status_code=422, detail="Пользователь с таким именем существует")
                if i["email"] == user.email:
                    raise HTTPException(status_code=422, detail="Пользователь с такой почтой существует")
            with open(path_id, 'r', encoding="utf-8") as file:
                data_id = json.load(file)
                data_id["id"] += 1
            id_ = data_id["id"]
            new_user = {
                "id": id_,
                "username": user.username,
                "email": user.email,
                "password": user.password
            }
            data.append(new_user)


        with open(path_id, 'w', encoding="utf-8") as file:
            file.write(json.dumps(data_id))

        with open(path_data, 'w', encoding="utf-8") as file:
            file.write(json.dumps(data))
        return f"User {user.username} registered successfully!"

    def get_all_user(self):
        path = "core//bd//user.json"
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data
        
    def get_by_id(self, id: int):
        path = "core//bd//user.json"
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for i in data:
                if i["id"] == id:
                    return i
        raise HTTPException(status_code=422, detail="Пользователя с таким id нет!")
