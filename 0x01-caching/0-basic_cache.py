#!/usr/bin/python3
"""BaseCaching module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
