from typing import List
import random


# to do: ml model
class RecModel():

    def __init__(self, songs: List[str]) -> None:
        self.library = songs

    def get_rec(self, user_songs: List[str], num: int = 5) -> List[str]:
        available = list(set(self.library) - set(user_songs))
        recs = random.sample(available, min(num, len(available)))
        return recs


rec_model = RecModel([f'song{i+1}' for i in range(10)])
