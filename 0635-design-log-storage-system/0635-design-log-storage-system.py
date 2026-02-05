from sortedcontainers import SortedList

class LogSystem:
    def __init__(self):
        self.logs = SortedList()
        self.indices = {
            "Year": 4, "Month": 7, "Day": 10, 
            "Hour": 13, "Minute": 16, "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.add((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.indices[granularity]
        min_suffix = "2000:01:01:00:00:00"
        max_suffix = "2017:12:31:23:59:59"
        
        start_full = start[:idx] + min_suffix[idx:]
        end_full   = end[:idx]   + max_suffix[idx:]
        
        # --- Step 1: Find the Left Index ---
        # We need the first log that is >= start_full.
        # We pair it with -1 because -1 is strictly smaller than any valid ID (>= 1).
        # Comparison: (Time, -1) < (Time, 1)
        # This guarantees we land BEFORE the first log with this timestamp.
        left_index = self.logs.bisect_left((start_full, -1))
        
        # --- Step 2: Find the Right Index ---
        # We need the insertion point AFTER the last log that is <= end_full.
        # We pair it with float('inf') because it is strictly larger than any valid ID.
        # Comparison: (Time, 500) < (Time, infinity)
        # This guarantees we land AFTER the last log with this timestamp.
        right_index = self.logs.bisect_right((end_full, float('inf')))
        
        # --- Step 3: Iterate / Slice ---
        # Now we can just slice the sorted list using these indices.
        # SortedList slicing is efficient.
        return [x[1] for x in self.logs[left_index:right_index]]