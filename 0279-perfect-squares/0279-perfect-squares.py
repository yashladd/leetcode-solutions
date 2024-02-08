class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float("inf")] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for t in range(1, n+1):
            s = 1
            while s*s <= t:
                dp[t] = min(dp[t], 1 + dp[t-s*s])
                s += 1
        return dp[n]