import json
import unittest
from fastapi.testclient import TestClient
from src.consumer import Consumer
from src.main import app
import src.routers as router
import src.contracts as contracts
from parameterized import parameterized


class TestRabbit(unittest.TestCase):
    client = TestClient(app)
    server = Consumer()

    def setUp(self):
        router.register(contracts.User(login='user2', password='user2'))
        router.song_like(contracts.Song(login='user2', fav_song='song1'))
        router.song_like(contracts.Song(login='user2', fav_song='song2'))
        router.song_like(contracts.Song(login='user2', fav_song='song3'))

    def test_send(self):
        response = self.client.post('/recs', login='user2')
        self.assertEqual(response.status_code, 200)

    @parameterized.expand([
        (['song1', 'song2', 'song3'])
    ])
    def test_server(self, songs):
        recs = self.server.callback(
            None, None, None,
            json.dumps({
                "login": 'user2', "user_songs": songs
            })
        )
        self.assertEqual(len(recs), 5)
        self.assertEqual(len(set(songs) & set(recs)), 0)
