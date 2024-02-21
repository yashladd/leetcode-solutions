class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.a = []
        

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        idx = len(self.a)
        self.h[val] = idx
        self.a.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.h:
            if self.h[val] != len(self.a)-1:
                idx, last = self.h[val], len(self.a) - 1
                self.h[self.a[last]] = idx
                self.a[idx], self.a[last] = self.a[last], self.a[idx]
            self.a.pop()
            del self.h[val]
            return True
        return False
        

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.a)-1)
        return random.choice(self.a)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()