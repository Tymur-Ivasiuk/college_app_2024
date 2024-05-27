from fastapi import FastAPI

from api.endpoints.auth.user import auth_router, register_router
from api.endpoints.auth.role import router as role_router
from api.endpoints.management.users_management import personal_router

import uvicorn

app = FastAPI(
    title="College App",
    description="Ivasiuk Tymur Diplom 2024",
)

app.include_router(
    auth_router,
    prefix="/users/jwt",
    tags=["Auth"]
)
app.include_router(
    register_router,
    prefix="/users",
    tags=["Auth"]
)

app.include_router(
    role_router,
    prefix="/role",
    tags=["Auth"]
)

app.include_router(personal_router)


@app.get("/", tags=["Test"])
def ping():
    return {
        "response": "pong"
    }




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

