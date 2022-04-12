import asyncio
import asyncpg
from fastapi import HTTPException

from loggers import exception_logging
from asyncpg import Record

db_conf = {'user': 'postgres', 'password': '12345678', 'database': 'fastapitest', 'host': '127.0.0.1'}


class DbConnection:

    def __init__(self):
        self.user = db_conf['user']
        self.password = db_conf['password']
        self.database = db_conf['database']
        self.host = db_conf['host']

    async def __aenter__(self): #setting up a connection
        self.conn = await asyncpg.connect(user=self.user, password=self.password, database=self.database, host=self.host)
        return self.conn

    async def __aexit__(self, exc_type, exc, tb): #closing the connection
        await self.conn.close()


async def db_fetch(query: str) -> list:
    async with DbConnection() as conn:
        records = await conn.fetch(query)
        records = [dict(r) for r in records]
        return records


async def db_get_row(query: str) -> dict:
    async with DbConnection() as conn:
        record = await conn.fetchrow(query)
        if record is None:
            raise HTTPException(status_code=404, detail='object does not exist')
        return dict(record)


async def db_execute(query: str) -> bool:
    async with DbConnection() as conn:
        await conn.execute(query)
        return True

