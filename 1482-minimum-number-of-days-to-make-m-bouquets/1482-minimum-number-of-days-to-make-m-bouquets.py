class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def canMake(days):
            nonlocal n
            boq = 0
            flow = 0
            for d in bloomDay:
                if d <= days:
                    flow += 1
                else:
                    boq += (flow//k)
                    flow = 0
                if boq == m:
                    return True
                    
            boq += (flow//k)
            return boq >= m
        
        lo = min(bloomDay)
        hi = max(bloomDay)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if(canMake(mid)):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return ans
                
            
                    
        