class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def canMake(days):
            nonlocal n
            bloomed = list(map(lambda x: x <= days, bloomDay))
            boq = 0
            i = 0;
            while i < n:
                if boq == m:
                    return True
                if bloomed[i]:
                    flow = 1
                    while i + 1 < n and bloomed[i+1] and flow < k:
                        i += 1
                        flow += 1
                    if flow == k:
                        boq += 1
                    i += 1
                else:
                    i += 1
                   
            return boq >= m
        
        
        lo = 1
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
                
            
                    
        