from fastapi import APIRouter
import src.contracts as contracts
from src.type.user import User
from src.database import repo
import pika
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()


@router.post('/register')
def register(user: contracts.User) -> None:
    if User(user.login, []) not in repo.list():
        repo.add(User(user.login, []))


@router.get("/register/list")
def get_users():
    return repo.list()


@router.post("/like")
def song_like(user_song: contracts.Song) -> None:
    repo.add_song(user_song.login, user_song.fav_song)


@router.get("/like/list")
def get_songs(login: str):
    return repo.get(login).songs


@router.post("/recs")
def send_task(login: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='gen_recs', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='gen_recs',
        body=json.dumps({
            "user": login,
            "user_songs": repo.get(login).songs
        })
    )
    logger.info(f'{login} recs have been requested')
