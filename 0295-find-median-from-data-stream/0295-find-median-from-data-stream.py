class MedianFinder:

    def __init__(self):
        self.minH = []
        self.maxH = []
        

    def addNum(self, num: int) -> None:
        heappush(self.maxH, -num)
        
        #Every element in maxH <= minH
        if (self.maxH and self.minH) and (-self.maxH[0] > self.minH[0]):
                num = -heappop(self.maxH)
                heappush(self.minH, num)
                
        #Their lengths differ by atmost 1
        if abs(len(self.maxH) - len(self.minH)) > 1:
            if len(self.maxH) > len(self.minH):
                num = -heappop(self.maxH)
                heappush(self.minH, num)
            else:
                num = heappop(self.minH)
                heappush(self.maxH, -num)
        

    def findMedian(self) -> float:
        if len(self.minH) == len(self.maxH):
            return (-(self.maxH[0]) + self.minH[0]) / 2
        elif len(self.minH) > len(self.maxH):
            return self.minH[0]
        else:
            return -self.maxH[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()