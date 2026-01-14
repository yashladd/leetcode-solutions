class CustomStack:
    def __init__(self, maxSize: int):
        self.s = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.s) < self.maxSize:
            self.s.append([x, 0])

    def pop(self) -> int:
        if len(self.s) == 0:
            return -1

        out, inc = self.s.pop()
        if len(self.s) > 0:
            self.s[-1][1] += inc
        return out + inc

    def increment(self, k: int, val: int) -> None:
        if len(self.s) >= k:
            self.s[k - 1][1] += val
        elif len(self.s) > 0:
            self.s[-1][1] += val