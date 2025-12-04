class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
    
    def balance(self):
        smSz, lrSz = len(self.small), len(self.large)
        if 1 + lrSz < smSz:
            heappush(self.large, -heappop(self.small))
        elif lrSz > smSz:
            heappush(self.small, -heappop(self.large)) 

    def addNum(self, num: int) -> None:
        if not self.small or -self.small[0] >= num:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)

        self.balance()
        
        
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()