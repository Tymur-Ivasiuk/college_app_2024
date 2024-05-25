from fastapi import FastAPI
from fastapi import APIRouter

import uvicorn

app = FastAPI(
    title="College App",
    description="Ivasiuk Tymur Diplom 2024",

)


@app.get("/", tags=["Test"])
def hello():
    return "Hello"




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

