#!/usr/bin/env python3
'''
BasicCache definition
'''
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    '''
    BasicCache that inherits from BaseCaching and is a caching system:
    '''
    def __init__(self):
        '''Initialize
        '''
        super().__init__()

    def put(self, key, item):
        '''Inserts an item into a dictionary
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Retrieves from cache
        '''
        return self.cache_data.get(key, None)
