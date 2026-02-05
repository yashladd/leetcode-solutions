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
        # Determine the slice length based on granularity
        idx = self.indices[granularity]
        
        # Truncate start and end times to the required granularity
        s_cut = start[:idx]
        e_cut = end[:idx]
        
        res = []
        for id, timestamp in self.logs:
            # Truncate the log's timestamp and compare lexicographically
            if s_cut <= timestamp[:idx] <= e_cut:
                res.append(id)
                
        return res