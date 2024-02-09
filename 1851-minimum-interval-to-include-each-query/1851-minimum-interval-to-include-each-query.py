class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        m = {i: v for i, v in enumerate(queries)}
        h = []
        i = 0
        res = [-1] * len(queries)
        for idx, val in sorted(m.items(), key = lambda x: x[1]):
            while i  < n and intervals[i][0] <= val:
                heappush(h, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            if h and h[0][1] >= val:
                res[idx] = h[0][0]
                continue
            
            while h and h[0][1] < val:
                heappop(h)
            
            if h:
                res[idx] = h[0][0]
                
        return res
            
        
        