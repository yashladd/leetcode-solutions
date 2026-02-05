class LogSystem:

    def __init__(self):
        self.logs = []
        # Map each granularity to the length of the string index we need to slice.
        # Format: Year:Month:Day:Hour:Minute:Second
        # Lengths correspond to:
        # Year (4) -> "2017"
        # Month (7) -> "2017:01"
        # Day (10) -> "2017:01:01"
        # ...and so on.
        self.indices = {
            "Year": 4, 
            "Month": 7, 
            "Day": 10, 
            "Hour": 13, 
            "Minute": 16, 
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        # Store the id and timestamp as a tuple
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        idx = self.indices[granularity]
        
        # Suffixes representing the smallest and largest possible values
        # We assume range 2000-2017 based on constraints, but 1999/2099 works too as bounds
        min_suffix = "2000:01:01:00:00:00"
        max_suffix = "2017:12:31:23:59:59"
        
        # Construct the full range strings ONCE
        # Take the user's prefix + the rest from our min/max templates
        start_full = start[:idx] + min_suffix[idx:]
        end_full   = end[:idx]   + max_suffix[idx:]
        
        res = []
        for id, timestamp in self.logs:
            # Now we compare full strings. No slicing needed inside the loop!
            if start_full <= timestamp <= end_full:
                res.append(id)
                
        return res