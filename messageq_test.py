import pytest
from queue import Queue
from .messageq import QueueWrapper
from unittest.mock import MagicMock


def teardown_function():
    import logging
    loggers = [logging.getLogger()] + list(logging.Logger.manager.loggerDict.values())
    for logger in loggers:
        handler = getattr(logger, 'handlers', [])
        for handler in handlers:
            logger.removeHandler(handler)

@pytest.fixture(scope='function')
def queue_wrapper():
    return QueueWrapper('testq', q=Queue())


def test_empty(queue_wrapper):
    assert queue_wrapper.q.size() == 0
    assert queue_wrapper.empty
    queue_wrapper.put('message')
    assert queue_wrapper.q.size() == 1