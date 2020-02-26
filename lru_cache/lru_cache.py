# Least Recently Used 1 2 3 4 -- Add 0 adds to front, evict an item based on the evict policy least recently used is 4.
# When we access a value in the new cache 0 1 2 3 the item moves to the front of the cache, it is the most accessed item
# A cache is a structure of data used for quick data reference. DLL --> Fast Lookup, Fast removal
# 0 1 2 3 4 5 6 7 8 9 10
import _collections


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.cache = _collections.OrderedDict()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        try:
            # pop the key off
            value = self.cache.pop(key)
            # set value to the front
            #  1,2,3,4 will become 4,1,2,3
            self.cache[key] = value
            return value
        # KeyError happens when key is not in dictionary
        except KeyError:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        try:
            # if key exists, pop 4 and insert to front
            self.cache.pop(key)
        # KeyError happens when key is not in dictionary
        except KeyError:
            # if length of cache is >= limit
            if len(self.cache) >= self.limit:
                # pop off last item and follow FIFO
                self.cache.popitem(last=False)
        # cache with key passed in is the value
        self.cache[key] = value
