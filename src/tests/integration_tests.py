import unittest
from src.main import app
from fastapi.testclient import TestClient


class IntegrationTests(unittest.TestCase):
    client = TestClient(app)

    def test_reg(self):
        response = self.client.get('/register/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'login': 'admin', 'songs': ['song1']}])

        self.client.post(
            '/register',
            json={'login': 'user1', 'password': 'user1'}
        )

        response = self.client.get('/register/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [{'login': 'user1', 'songs': []}, {'login': 'admin', 'songs': ['song1']}]
        )

    def test_like(self):
        self.client.post(
            '/like',
            json={'login': 'admin', 'fav_song': 'song1'}
        )
        response = self.client.get('/like/list?login=admin')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), ['song1'])

    def test_recs(self):
        response = self.client.get('/recs?login=admin')
        user_songs = self.client.get('/like/list?login=admin')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(len(set(response.json()) & set(user_songs)), 0)
