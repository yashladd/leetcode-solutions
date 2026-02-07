class MyCalendarThree:

    def __init__(self):
        self.events = SortedList()
        

    def book(self, start: int, end: int) -> int:
        cnt = 0
        self.events.add((start, 1))
        self.events.add((end, -1))
        k = 0
        for time, val in self.events:
            # print(time, val)
            cnt += val
            k = max(k, cnt)

        return k






# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)