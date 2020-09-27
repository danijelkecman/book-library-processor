'''
    This module allows us to have a centralized logger that will be used
    from multiple processes at the same time
'''

from multiprocessing improt get_logger
import logging


def logger(level=logging.INFO) -> logging.Logger:
    log = get_logger()
    log.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatting(logging.Formatter(
        '%(levelname)s: %(asctime)s - %(process)s - %(message)s'
    ))
    log.addHandler(handler)
    return log


# Exposing app_logger to be used by other modules
app_logger = logger()