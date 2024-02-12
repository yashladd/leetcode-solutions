class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def canMake(d):
            a = [1 if bloomDay[i] <= d else 0 for i in range(len(bloomDay))]
            cnt = 0
            i = 0 
            while i < len(a):
                if not a[i]:
                    i += 1
                    continue
                else:
                    fl = 1
                    i += 1
                    while i < len(a) and a[i] and fl < k:
                        fl += 1
                        i += 1
                    if fl == k:
                        cnt += 1
            return cnt >= m
        
        l, r = 1, max(bloomDay)
        
        ans = -1
        while l <= r:
            mid = (l + r) >> 1
            if canMake(mid):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        return ans
            
                        
                        
            
        