class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        """
        dec at index = numOpsThusFar * y - timesIndexWasLargest * x  + timesIndexWasLargest * y

        How to calc 
        - Maybe max heap to store largest number
        - Keep ops variable
        - if Decrease of num <= 0 remove from heap  
        """

        def canReduce(k, x, y):
            remain = [num - k * y for num in nums]

            numOps = 0

            for r in remain:
                if r > 0:
                    numOps += math.ceil((r)/(x-y))
                    if numOps > k:
                        return False

            return numOps <= k

        lo, hi = 0, math.ceil(max(nums) / y)

        while lo < hi:
            m = (lo + hi) >> 1
            if canReduce(m, x, y):
                hi = m
            else:
                lo = m + 1
        return hi