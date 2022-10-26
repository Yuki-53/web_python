import json
import logging

import pika
from recsys import rec_model


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Consumer():
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='gen_recs', durable=True)

    def callback(self, ch, method, properties, body):
        """
        Consumer get data and make recs
        """
        data = json.loads(body.decode())
        login = data['login']
        user_songs = data['user_songs']
        logger.info(f'{login} data received')
        recs = rec_model.get_rec(user_songs)
        logger.info(f'{login} recs get')
        return recs  # for tests

    def listen(self):
        self.channel.basic_consume(queue='gen_recs', on_message_callback=self.callback)
        self.channel.start_consuming()

    def stop(self):
        self.channel.stop_consuming()
        self.connection.close()


if __name__ == "__main__":
    server = Consumer()
    server.listen()
