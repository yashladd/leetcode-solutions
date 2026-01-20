class OrderedStream:

    def __init__(self, n: int):
        self.values = [None] * (n + 1)
        self.idx =  1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        res = []
        while self.idx < len(self.values) and self.values[self.idx] != None:
            res.append(self.values[self.idx])
            self.idx += 1

        return res

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)