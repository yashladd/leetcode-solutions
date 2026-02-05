import bisect

class LogSystem:

    def __init__(self):
        # We will keep this list SORTED by timestamp
        self.logs = []
        
        self.indices = {
            "Year": 4, "Month": 7, "Day": 10, 
            "Hour": 13, "Minute": 16, "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        # bisect.insort inserts the element while maintaining the sorted order.
        # This acts like the TreeMap.put() but is O(N) in Python due to list shifting.
        bisect.insort(self.logs, (timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.indices[granularity]
        
        # 1. Define bounds
        min_suffix = "2000:01:01:00:00:00"
        max_suffix = "2017:12:31:23:59:59"
        
        start_full = start[:idx] + min_suffix[idx:]
        end_full   = end[:idx]   + max_suffix[idx:]
        
        # 2. Binary Search for BOTH ends
        # Left: First index where (timestamp, id) >= (start_full, -infinity)
        left = bisect.bisect_left(self.logs, (start_full, -1))
        
        # Right: First index where (timestamp, id) > (end_full, +infinity)
        # This effectively gives us the index 'after' the last valid element.
        right = bisect.bisect_right(self.logs, (end_full, float('inf')))
        
        # 3. Slice and Extract
        # Slicing in Python [left:right] is very efficient (implemented in C)
        return [x[1] for x in self.logs[left:right]]