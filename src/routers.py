from fastapi import APIRouter
import src.contracts as contracts
from src.type.user import User
from src.database import repo
from src.recsys import rec_model

router = APIRouter()


@router.post('/register')
def register(user: contracts.User) -> None:
    if User(user.login, []) not in repo.list():
        repo.add(User(user.login, []))


@router.post("/like")
def song_like(user_song: contracts.Song) -> None:
    repo.add_song(user_song.login, user_song.fav_song)


@router.get("/recs")
def get_recs(login: str, num: int):
    return rec_model.get_rec(repo.get(login).songs, num)
