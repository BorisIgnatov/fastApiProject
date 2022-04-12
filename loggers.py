import logging

from fastapi import HTTPException

db_logger = logging.Logger(name='db_logger')


def exception_logging(func):
    async def wrapper(*args):
        try:
            return await func(*args)
        except Exception as e:
            db_logger.error(f'Exception occured in {func.__name__}. e - {str(e)}')
    return wrapper

