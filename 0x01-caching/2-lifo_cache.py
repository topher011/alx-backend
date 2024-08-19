#!/usr/bin/env python3
'''
LIFOCache that inherits from BaseCaching and is a caching system:
'''
from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    Definition of LIFO caching class
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.q = Queue()

    def put(self, key, item):
        '''
        Insert into LIFO dict
        '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.q.queue.pop()
                print("DISCARD: {}".format(discarded))
                self.cache_data.pop(discarded)
            self.q.put(key)

    def get(self, key):
        '''
        Retrieving from dict
        '''
        return self.cache_data.get(key)
