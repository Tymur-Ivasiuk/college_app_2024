import uvicorn

from fastapi import FastAPI

from api.endpoints.users.auth.user_endpoints import auth_router
from api.endpoints.users.personal_management import personal_router
from api.endpoints.structures.structures_management import structures_router

app = FastAPI(
    title="College App",
    description="Ivasiuk Tymur Diplom 2024",
)

app.include_router(auth_router)

app.include_router(personal_router)
app.include_router(structures_router)


@app.get("/", tags=["Test"])
def ping():
    return {
        "response": "pong"
    }




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

