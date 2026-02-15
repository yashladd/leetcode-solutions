import bisect

class MyCalendar:
    def __init__(self):
        # List of [start, end] pairs, kept sorted by start time
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        # 1. Find the index where this event would be inserted to keep list sorted
        # We search by startTime
        idx = bisect.bisect_left(self.calendar, [startTime, endTime])
        
        # 2. Check overlap with the NEXT event
        # The next event is currently at index 'idx'
        if idx < len(self.calendar):
            next_start, next_end = self.calendar[idx]
            if startTime < next_end and next_start < endTime:
                return False
        
        # 3. Check overlap with the PREVIOUS event
        # The previous event is at index 'idx - 1'
        if idx > 0:
            prev_start, prev_end = self.calendar[idx - 1]
            if prev_start < endTime and startTime < prev_end:
                return False
        
        # 4. No overlap found, insert the event and return True
        self.calendar.insert(idx, [startTime, endTime])
        return True