#!/usr/bin/env python3
'''
MRUCache that inherits from BaseCaching and is a caching system:
'''
from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    Definition of MRU caching class
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.q = Queue()

    def put(self, key, item):
        '''
        Insert into MRU dict
        '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.q.queue.pop()
                print("DISCARD: {}".format(discarded))
                del self.cache_data[discarded]
            if key not in self.q.queue:
                self.q.put(key)

    def get(self, key):
        '''
        Retrieving from dict
        '''
        if key in self.cache_data:
            self.q.queue.remove(key)
            self.q.queue.append(key)
        return self.cache_data.get(key, None)
