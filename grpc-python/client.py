import grpc

from definitions.builds.service_pb2 import Genre
from definitions.builds.service_pb2_grpc import TestServiceStub


def main():
    '''
    Recieve data from server
    '''
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        song = client.get_songs(Genre(
            genre_name="rock"
        ))

        print(song.song_name)


if __name__ == "__main__":
    main()
