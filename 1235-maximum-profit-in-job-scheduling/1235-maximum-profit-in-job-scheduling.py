class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = []
        starts = []
        for s, e, p in zip(startTime, endTime, profit):
            intervals.append((s, e, p))
            starts.append(s)
            
        intervals = sorted(intervals, key=lambda x: x[0])
        starts.sort()
        n = len(intervals)
        dp = [0] * (n + 1)
        for index in range(n-1, -1, -1):
            notTake = dp[index + 1]
            take = intervals[index][2]
            take += dp[bisect_left(starts, intervals[index][1])]
            dp[index] = max(take, notTake)

        return dp[0]

        
        def maximizePrice(index):
            if index >= n:
                return 0
            if dp[index] != -1:
                return dp[index]
            notTake = maximizePrice(index + 1)
            take = intervals[index][2]
            ## USE BS TO FIND THE NEXT INDEX
            nextIdx = bisect_left(starts, intervals[index][1])
            
            take += maximizePrice(nextIdx)
            dp[index] = max(take, notTake)
            return dp[index]
        
        return maximizePrice(0)
        