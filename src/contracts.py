from pydantic import BaseModel


class RequestBody(BaseModel):
    name: str
    description: str | None = None
    value: float
