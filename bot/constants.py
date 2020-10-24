from os import environ
from typing import NamedTuple

__all__ = ('Config', 'Postgresql')


class Config(NamedTuple):
    TOKEN = environ.get('BOT_TOKEN')


class Postgresql(NamedTuple):
    USER = environ.get('POSTGRES_USER')
    PASSWORD = environ.get('POSTGRES_PASSWORD')
    DATABASE = environ.get('POSTGRES_DB')
    HOST = environ.get('POSTGRES_HOST')

    asyncpg_config = {'user': USER, 'password': PASSWORD, 'database': DATABASE, 'host': HOST}
