class MyCalendar:

    def __init__(self):
        self.a = []

    def book(self, s: int, e: int) -> bool:
        for i in range(len(self.a)):
            ps, pe = self.a[i]
            if e > ps and s < pe:
                return False
        self.a.append((s,e))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)