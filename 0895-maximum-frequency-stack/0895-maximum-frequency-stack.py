class FreqStack:

    def __init__(self):
        self.hashStack = defaultdict(list)
        self.frequency = defaultdict(int)
        self.maxF = 0
        

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.hashStack[self.frequency[val]].append(val)
        self.maxF = max(self.maxF, self.frequency[val])
    
    def pop(self) -> int:
        val = self.hashStack[self.maxF].pop()
        self.frequency[val] -= 1
        while self.maxF and not self.hashStack[self.maxF]:
            self.maxF -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()