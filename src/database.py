import abc
from typing import List
from src.type.user import User


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError


class UserRepository(AbstractRepository):
    def __init__(self, users: List[User]):
        self._users = set(users)

    def add(self, user: User):
        self._users.add(user)

    def add_song(self, login: str, song_name: str):
        user: User = next(b for b in self._users if b.login == login)

        if user:
            user.songs.append(song_name)

    def get(self, id: str):
        return next(b for b in self._users if b.login == id)

    def list(self):
        return list(self._users)


def reset_data():
    repo = UserRepository([User('admin', [])])

repo = UserRepository([User('admin', [])])
