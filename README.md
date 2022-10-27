# FastAPI app

This app will recommend music tracks to users based on the user's favorite songs

Users can:
1) Register
2) Add favorite music
3) Get recommendations

## How to run
For install dependencies: `poetry install`

For launch app run: `uvicorn src.main:app --reload`

To run a RabbitMQ docker image: `docker compose up`

It is also necessary to set exchange, queue 'gen_recs' and the routing key 'gen_recs' in it (localhost:15672)

To start a consumer run: `python .\src\consumer.py`

## Testing
For launch unit tests run: `python -m unittest src/tests/unit_tests.py`

For launch integration tests run: `python -m unittest src/tests/integration_tests.py`

For launch broker tests run: `python -m unittest src/broker/tests/_\_init__.py`
