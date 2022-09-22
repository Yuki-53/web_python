from fastapi import APIRouter
from src import contracts

router = APIRouter()


@router.get("/")
def hello():  # noqa: D103
    return {"Hello": "World"}


@router.get("/hello/{name}")
def personal_hi(name: str):
    return {"Hello": name}


@router.get("/query")
def query(name: str, q: str | None = None):
    if q:
        return {"user": name, "msg": q}
    return {"user": name}


@router.post("/body")
def create_item(request: contracts.RequestBody):
    return {"Name": request.name,
            "Description": request.description,
            "Value": 0 if request.value < 0 else request.value}
