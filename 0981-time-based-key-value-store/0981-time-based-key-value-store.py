class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        a = self.m[key]
        l, h = 0, len(a) - 1
        while l <= h:
            m = (l + h) >> 1
            if a[m][0] <= timestamp:
                res = a[m][1]
                l = m + 1
            else:
                h = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)