class TwoSum:

    def __init__(self):
        self.h = defaultdict(int)

    def add(self, number: int) -> None:
        self.h[number] += 1
        

    def find(self, value: int) -> bool:

        for k, v in self.h.items():
            if k == value - k:
                if self.h[k] > 1:
                    return True
            elif value - k in self.h:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)