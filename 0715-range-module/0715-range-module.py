import bisect

class RangeModule:
    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        # Find insertion points
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)
        
        # If 'i' is even, 'left' falls outside any existing interval, so we keep it.
        # If 'j' is even, 'right' falls outside any existing interval, so we keep it.
        self.track[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.track, left)
        j = bisect.bisect_left(self.track, right)
        
        # For a range to be fully covered, both left and right must fall 
        # inside the SAME existing interval (i == j) AND that interval 
        # must be currently tracked (i % 2 == 1).
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)
        
        # If 'i' is odd, 'left' falls inside an interval, we need to close it at 'left'.
        # If 'j' is odd, 'right' falls inside an interval, we need to open it at 'right'.
        self.track[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)