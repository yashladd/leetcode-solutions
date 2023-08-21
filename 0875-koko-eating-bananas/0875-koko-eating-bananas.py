class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hrs = 0
            for p in piles:
                hrs += (ceil(p/k))
            # print(h)
            return hrs <= h
        
        lo, hi = 1, max(piles)
        ans = 0
        while lo <= hi:
            m = (lo + hi) >> 1
            if canEat(m):
                ans = m
                hi = m - 1
            else:
                lo = m + 1
                
        return ans
                    
                
        