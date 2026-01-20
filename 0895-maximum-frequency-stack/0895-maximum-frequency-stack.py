class FreqStack:

    def __init__(self):
        self.h = []
        self.cnt = defaultdict(int)
        self.idx = 0
        

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heappush(self.h, (-self.cnt[val], -self.idx, val))
        self.idx += 1
        

    def pop(self) -> int:
        _, _, val = heappop(self.h)
        self.cnt[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()