import time
import functools

import logging


def get_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s:%(lineno)i - %(levelname)s - %(message)s"
    )
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False
    return logger


logger = get_logger(__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f"{func.__name__} started")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.info(f"{func.__name__} finished, take {end - start} s")
            return result
        except Exception as e:
            logger.info(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e

    return wrapper


def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time

        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        logger.info("%s cost time: %.3f s" % (func.__name__, time_spend))
        return result

    return func_wrapper


def logit(logger: logging.Logger = None):
    def decorator(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            kwargs_ = ",".join(sorted(f"{k}={v}"[:36] for k, v in kwargs.items()))
            logger.debug(f"{func.__name__}({kwargs_}) started")

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            type_ = type(result)
            if isinstance(result, list):
                len_ = len(result)
                res_ = str(result[:1])[:80]
            else:
                len_ = None
                res_ = None
            result_ = f"type:{type_},len:{len_},head:{res_}"
            logger.debug(
                f"{func.__name__}({kwargs_}) finished|\ttake: {(end - start) * 1000:.3f} ms|\treturn: {result_}")
            return result

        return func_wrapper

    return decorator
