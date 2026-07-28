class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()
    

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        val = self._cache[key]

        del self._cache[key]

        self._cache[key] = val

        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            del self._cache[key]

            self._cache[key] = value

            return

        if len(self._cache) == self._capacity:
            self._cache.popitem(last=False)

        self._cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)