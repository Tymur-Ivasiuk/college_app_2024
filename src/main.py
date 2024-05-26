from fastapi import FastAPI
from auth.router import auth_router, register_router

import uvicorn

app = FastAPI(
    title="College App",
    description="Ivasiuk Tymur Diplom 2024",
)

app.include_router(
    auth_router,
    prefix="/users",
    tags=["Auth"]
)
app.include_router(
    register_router,
    prefix="/users",
    tags=["Auth"]
)


@app.get("/", tags=["Test"])
def hello():
    return "Hello"




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

