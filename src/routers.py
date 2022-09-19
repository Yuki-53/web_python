from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def hello():  # noqa: D103
    return "Hello world"


@router.get("/{name}")
def personal_hi(name: str):
    return f"Hello {name}"


@router.get("/query")
def query(param: str):
    return f"query: {param}"


@router.post("/body")
def request(body):
    return body
