class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = []
        for s, e, p in zip(startTime, endTime, profit):
            intervals.append((s, e, p))
            
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        
        n = len(intervals)
        
        dp = [-1] * n
        
        def f(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            notTake = f(i + 1)
            
            take = intervals[i][2]
            
            nextIdx = i + 1
            while nextIdx < n and intervals[nextIdx][0] < intervals[i][1]:
                nextIdx += 1
            # print(i, nextIdx)
            take += f(nextIdx)
            
            dp[i] = max(take, notTake)
            return dp[i]
        
        return f(0)
        