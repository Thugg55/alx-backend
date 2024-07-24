#!/usr/bin/python3
""" A class BasicCache that inherits from
BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class BaseCaching:
    def __init__(self):
        self.cache_data = {}


class BasicCache(BaseCaching):
    """A class object that allows storing and
    retrieving items from dict """
    def put(self, key, item):
        """An item is added in cache"""
        if key is None or item is None:
            self.cache_data.update({key: item})

    def get(self, key):
        """BY KEY, get an object"""
        if key is None:
            return None
        return self.cache_data.get(key)
