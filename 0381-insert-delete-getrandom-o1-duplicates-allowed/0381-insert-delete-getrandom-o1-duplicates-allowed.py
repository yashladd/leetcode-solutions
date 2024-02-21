class RandomizedCollection:

    def __init__(self):
        self.h = defaultdict(set)
        self.l = []
        

    def insert(self, val: int) -> bool:
        ret = val not in self.h
        insertIdx = len(self.l)
        self.h[val].add(insertIdx)
        self.l.append(val)
        return ret
        

    def remove(self, val: int) -> bool:
        """
            {1: (0)}

        """
        if val in self.h:
            remIdx = self.h[val].pop()
            lastIdx = len(self.l) - 1
            if remIdx == lastIdx:
                if not len(self.h[val]):
                    del self.h[val]
                self.l.pop()
                return True
            if not len(self.h[val]):
                del self.h[val]
            self.h[self.l[lastIdx]].remove(lastIdx)
            self.h[self.l[lastIdx]].add(remIdx)
            self.l[remIdx], self.l[lastIdx] = self.l[lastIdx], self.l[remIdx]
            self.l.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()