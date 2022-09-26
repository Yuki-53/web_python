from typing import List


class User:
    def __init__(self, login: str, fav_songs: List[str]) -> None:
        self.login = login
        self.songs = fav_songs

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.login == self.login and other.songs == self.songs

    def __hash__(self):
        return hash(self.login)
