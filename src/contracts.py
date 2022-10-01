from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str


class Song(BaseModel):
    login: str
    fav_song: str
