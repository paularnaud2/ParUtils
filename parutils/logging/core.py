from functools import wraps

from . import g
from .logger import Logger


def get_logger() -> Logger:

    if g.cur_logger is None:
        logger = Logger(file_write=False)
        g.cur_logger = logger
    else:
        logger = g.cur_logger
    return logger


def close_logger():

    if g.cur_logger:
        g.cur_logger.close()


def logger_methode(func):

    @wraps(func)
    def new(*args, **kwargs):
        logger = get_logger()
        logger_methode = getattr(logger, func.__name__)
        return logger_methode(*args, **kwargs)

    return new
