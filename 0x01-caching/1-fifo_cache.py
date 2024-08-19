#!/usr/bin/env python3
'''
FIFOCache that inherits from BaseCaching and is a caching system:
'''
from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    Definition of FIFO caching class
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.q = Queue()

    def put(self, key, item):
        '''
        Insert into FIFO dict
        '''
        if key and item:
            self.cache_data[key] = item
            self.q.put(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.q.queue.popleft()
                print("DISCARD: {}".format(discarded))
                self.cache_data.pop(discarded)

    def get(self, key):
        '''
        Retrieving from dict
        '''
        return self.cache_data.get(key)
