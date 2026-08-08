# from __future__ import annotations
from dataclasses import dataclass
@dataclass
class Node:
    start: int
    end: int
    left: Node | None = None
    right: Node | None = None


class MyCalendar:

    def __init__(self):
        self.root = None
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Node(startTime, endTime)
            return True

        curr = self.root

        while True:
            if endTime <= curr.start:
                if not curr.left:
                    curr.left = Node(startTime, endTime)
                    return True
                curr = curr.left
            elif startTime >= curr.end:
                if not curr.right:
                    curr.right = Node(startTime, endTime)
                    return True
                curr = curr.right
            else:
                return False

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)