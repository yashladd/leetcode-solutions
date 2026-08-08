from collections import defaultdict

class MyCalendarTwo:
    def __init__(self):
        # Stores the net change of active bookings at any given timestamp
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        # 1. Temporarily log the new event
        self.timeline[start] += 1
        self.timeline[end] -= 1
        
        active_bookings = 0
        
        # 2. Sweep through the timestamps in chronological order
        for time in sorted(self.timeline.keys()):
            active_bookings += self.timeline[time]
            
            # 3. If we hit a triple booking, ROLLBACK and return False
            if active_bookings >= 3:
                self.timeline[start] -= 1
                self.timeline[end] += 1
                
                # Cleanup zero-values to save memory (optional but shows good habits)
                if self.timeline[start] == 0:
                    del self.timeline[start]
                if self.timeline[end] == 0:
                    del self.timeline[end]
                    
                return False
                
        # 4. If the loop finishes safely, the booking is valid!
        return True