import uvicorn
from fastapi import FastAPI, Request, Response, Cookie
from fastapi.responses import ORJSONResponse, PlainTextResponse, RedirectResponse

#from .core.models.user import UserModel
from core.models.requests import UserRequest
from core.services import user_service
from core.models.requests import LoginRequest

app = FastAPI()

@app.get("/")
async def root():
    return {"massege": "Hello, World!"}

@app.get("/greet/{name}")
async def greet_func(name: str):
    return f"Hello, {name}"

@app.get("/search")
async def search_func(query: str):
    return f"You searched for: {query}"

@app.get("/json")
async def json_func(name: str, age: int, hobby:str):
    return ORJSONResponse([{
        "name": name,
        "age": age,
        "hobby": hobby
    }])

@app.get("/file", response_class=PlainTextResponse)
async def file_func(file_text: str):
    return file_text

@app.get("/redirect", response_class=RedirectResponse)
async def redirect_func():
    return "/"

@app.get("/headers")
async def headers_func(request: Request):
    return request.headers

@app.get("/set-cookie")
async def set_cookie_func(response: Response, username: str):
    response.set_cookie(key="username", value=username, max_age=60)
    return "Куки установлен!"

@app.get("/get-cookie")
async def get_cookie_func(username = Cookie(default=None)):
    if username == None:
        return "Такого куки нет, упс"
    return {"username": username}

@app.post("/register")
async def register_func(user: UserRequest):
    return user_service.add_data(user)

@app.get("/login")
async def login_func(username: str, password: str):
    return user_service.get_user(LoginRequest(username=username, password=password))

@app.get("/users", response_class=ORJSONResponse)
async def get_all_users():
    return user_service.get_all_user()

@app.get("/users/{id}")
async def get_user_by_id(id_):
    return user_service.get_by_id(int(id_))

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
