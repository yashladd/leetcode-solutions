class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        largestSmall = -heappop(self.small)

        heappush(self.large, largestSmall)

        if len(self.small) < len(self.large):
            smallestLarge = heappop(self.large)
            heappush(self.small, -smallestLarge)
        
        

    def findMedian(self) -> float:
        if len(self.small) != len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()