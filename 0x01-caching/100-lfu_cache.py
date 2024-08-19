#!/usr/bin/env python3
'''
LFUCache that inherits from BaseCaching and is a caching system:
'''
from queue import Queue
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    Definition of LFU caching class
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.q = {}

    def put(self, key, item):
        '''
        Insert into LFU dict
        '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                cache_entries = self.q.items()
                least_key, least = list(cache_entries)[0]
                for (key_q, value_q) in cache_entries:
                    if value_q < least:
                        least = value_q
                        least_key = key_q
                print("DISCARD: {}".format(least_key))
                del self.cache_data[least_key]
                del self.q[least_key]
            if key not in self.q:
                self.q[key] = 0
            else:
                self.q[key] += 1

    def get(self, key):
        '''
        Retrieving from dict
        '''
        if key in self.cache_data:
            self.q[key] += 1
        return self.cache_data.get(key, None)
