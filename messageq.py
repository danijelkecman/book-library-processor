'''
    This module provides us with a drainable multiprocess aware message queue.
'''

from multiprocessing import Event, Queue
from multiprocessing.managers import BaseManager
from queue import Empty
from typing import Any, List

from .debugging import app_logger as log


class QueueWrapper(object):

    def __init__(self, name: str, q: Queue = None, prevent_writes: Event = None):
        pass

    def connect(self):
        '''Connect to multiprocessing.Queue
        Used by clients attempting to connect to the queue via a proxt.
        '''
        pass