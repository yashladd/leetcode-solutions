from sortedcontainers import SortedList

class MyCalendarTwo:
    def __init__(self):
        # We use a SortedList just like in My Calendar III
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        # 1. Temporarily add the new event
        self.events.add((start, 1))
        self.events.add((end, -1))
        
        active_bookings = 0
        
        # 2. Run the sweep line to check for triple bookings
        for time, val in self.events:
            active_bookings += val
            
            # 3. If we hit a triple booking, ROLLBACK and fail
            if active_bookings >= 3:
                self.events.remove((start, 1))
                self.events.remove((end, -1))
                return False
                
        # 4. If we made it through safely, keep the booking!
        return True