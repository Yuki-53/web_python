from typing import List
import unittest
import grpc
from definitions.builds.service_pb2 import Genre
from definitions.builds.service_pb2_grpc import TestServiceStub
from parameterized import parameterized


class TestResponse(unittest.TestCase):
    @parameterized.expand([
        ('rock', [f'song_{i+1}' for i in range(10)]),
        ('pop', [f'another_song_{i+1}' for i in range(10)]),
    ])
    def test_get_song(self, genre: str, expected: List[str]):
        client = TestServiceStub(grpc.insecure_channel("localhost:3000"))
        response = client.get_songs(Genre(
            genre_name=genre
        ))
        self.assertTrue(response.song_name in expected)
