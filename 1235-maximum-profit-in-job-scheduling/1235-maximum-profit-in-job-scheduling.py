class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = []
        for s, e, p in zip(startTime, endTime, profit):
            intervals.append((s, e, p))
            
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        dp = [-1] * n
        
        def maximizePrice(index):
            if index >= n:
                return 0
            if dp[index] != -1:
                return dp[index]
            notTake = maximizePrice(index + 1)
            take = intervals[index][2]
            nextIdx = index + 1
            while nextIdx < n and intervals[nextIdx][0] < intervals[index][1]:
                nextIdx += 1
            take += maximizePrice(nextIdx)
            dp[index] = max(take, notTake)
            return dp[index]
        
        return maximizePrice(0)
        