class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def canEat(r):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/r)
            return hrs <= h
        
        lo, hi = 1, max(piles)
        ans = hi
        while lo <= hi:
            m = (lo + hi) >> 1
            if canEat(m):
                ans = m
                hi = m-1
            else:
                lo = m + 1
                
        return ans
        