from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.events = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        if not len(self.events):
            self.events.add((startTime, endTime))
            return True

        idx = bisect_right(self.events, (startTime, endTime))

        if (idx - 1 >= 0 and self.events[idx-1][1] > startTime) or (idx < len(self.events) and self.events[idx][0] < endTime):
            return False

        self.events.add((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)