class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)        
        dp = {}
        events = sorted(events, key=lambda x: x[0])
        S = [events[i][0] for i in range(n)]
        
        def f(i, k):
            if k == 0:
                return 0
            
            if i >= n:
                return 0
            
            if (i, k) in dp:
                return dp[(i, k)]
            
            
            nt = f(i + 1, k)
            
            nex = bisect_left(S, events[i][1] + 1)
            
            t = events[i][2] + f(nex, k-1)
            
            dp[(i, k)] = max(t, nt)
            return dp[(i, k)]
        
        return f(0, k)
            
            