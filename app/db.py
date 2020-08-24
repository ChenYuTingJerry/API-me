import abc

from gino import Gino
from sqlalchemy.engine.url import URL
from uvloop import Loop


class AsyncDatabaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def init(self, loop: Loop):
        raise NotImplementedError

    @abc.abstractmethod
    async def connect(self, db_settings: dict):
        raise NotImplementedError

    @abc.abstractmethod
    async def close(self):
        raise NotImplementedError


class GinoPostgresDB(AsyncDatabaseInterface):
    engine = Gino()

    def __init__(self):
        self._loop = None

    def init(self, loop: Loop):
        self._loop = loop

    async def connect(self, db_settings: dict):
        dsn = URL(
            drivername=db_settings.setdefault("DB_DRIVER", "asyncpg"),
            host=db_settings.setdefault("DB_HOST", "localhost"),
            port=db_settings.setdefault("DB_PORT", 5432),
            username=db_settings.setdefault("DB_USER", "postgres"),
            password=db_settings.setdefault("DB_PASSWORD", ""),
            database=db_settings.setdefault("DB_DATABASE", "postgres"),
        )
        await self.engine.set_bind(
            dsn,
            echo=db_settings.setdefault("DB_ECHO", False),
            min_size=db_settings.setdefault("DB_POOL_MIN_SIZE", 5),
            max_size=db_settings.setdefault("DB_POOL_MAX_SIZE", 10),
            ssl=db_settings.setdefault("DB_SSL"),
            loop=self._loop,
        )

    async def close(self):
        await self.engine.pop_bind().close()

    @property
    def Model(self) -> Gino.Model:
        return self.engine.Model

    @property
    def Schema(self):
        return self.engine


pg = GinoPostgresDB()
