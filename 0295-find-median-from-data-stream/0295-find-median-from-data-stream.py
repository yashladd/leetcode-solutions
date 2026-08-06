class MedianFinder:

    def __init__(self):
        self._small = []
        self._large = []


    def _balance(self):
        if len(self._large) > len(self._small):
            heappush(self._small, -heappop(self._large)) 

        if len(self._small) > 1 + len(self._large):
            heappush(self._large, -heappop(self._small))



    def addNum(self, num: int) -> None:
        if not self._small or num <= -self._small[0]:
            heappush(self._small, -num)
        else:
            heappush(self._large, num)

        self._balance()


    def findMedian(self) -> float:
        if len(self._small) == len(self._large):
            return (-self._small[0] + self._large[0]) / 2.0
        
        return -self._small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()