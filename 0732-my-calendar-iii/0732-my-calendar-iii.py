from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        # Stores the net change of active bookings at any given timestamp
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        # 1. Temporarily log the new event
        self.timeline[start] += 1
        self.timeline[end] -= 1
        
        max_bookings = 0
        active_bookings = 0
        # 2. Sweep through the timestamps in chronological order
        for time in sorted(self.timeline.keys()):
            active_bookings += self.timeline[time]
            
            # 3. If we hit a triple booking, ROLLBACK and return False
            max_bookings = max(max_bookings, active_bookings)
                
        # 4. If the loop finishes safely, the booking is valid!
        return max_bookings