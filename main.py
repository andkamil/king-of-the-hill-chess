from fastapi import FastAPI

from user.router import user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
async def test():
    return "Hello World"