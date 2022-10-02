from concurrent.futures import ThreadPoolExecutor

import grpc
import random

from definitions.builds.service_pb2 import Song
from definitions.builds.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server


class Service(TestServiceServicer):

    def get_songs(self, request, context):
        """
        func return a song of a specific genre
        """
        if request.genre_name == 'rock':
            expected_name = random.choise([f'song_{i+1}' for i in range(10)])
        elif request.genre_name == 'pop':
            expected_name = random.choise([f'another_song_{i+1}' for i in range(10)])
        return Song(song_name=expected_name)


def execute_server():
    """ 
    Start grpc server
    """
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
