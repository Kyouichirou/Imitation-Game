__all__ = ['Logs']

import os
import time
from loguru import logger

# @author: hla
# @update: 2022-09-05
# @finished_state: 1
# @description: 日志记录, 更为友好的日志记录-loguru
# @name: 日志记录


class Logs:
    _instance = None

    @staticmethod
    def _time_stamp():
        return str(int(time.time()))

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logs, cls).__new__(cls, *args, **kwargs)
            path = os.getcwd() + fr'\log_{cls._time_stamp()}.log'
            logger.add(path, rotation="5MB", encoding="utf-8", enqueue=True, backtrace=True, diagnose=True)
        return cls._instance

    @staticmethod
    def info(msg):
        logger.info(msg)

    @staticmethod
    def debug(msg):
        logger.debug(msg)

    @staticmethod
    def warning(msg):
        logger.warning(msg)

    @staticmethod
    def error(msg):
        logger.error(msg)

    @staticmethod
    def capture_except(msg):
        logger.exception(msg)

    def decorator(self, msg):
        def decorator_log(func):
            def wrapper(*args, **kwargs):
                # noinspection PyBroadException
                # 不提示广泛exception
                try:
                    return func(*args, **kwargs)
                except Exception:
                    self.capture_except(msg)
                    return None

            return wrapper

        return decorator_log


if __name__ == '__main__':
    _logger = Logs()
    # noinspection PyBroadException
    try:
        print(1 / 0)
    except Exception:
        _logger.capture_except('test')
