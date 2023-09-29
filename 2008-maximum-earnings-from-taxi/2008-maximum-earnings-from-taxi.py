class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        n = len(rides)
        dp = [-1] * n
        rides = sorted(rides, key=lambda x: x[0])
        starts = [rides[i][0] for i in range(n)]
        def f(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            nt = f(i + 1)
            
            nex = bisect_left(starts, rides[i][1])
            
            take = rides[i][1] - rides[i][0] + rides[i][2] + f(nex)
            
            dp[i] = max(nt, take)
            return dp[i]
        
        return f(0)