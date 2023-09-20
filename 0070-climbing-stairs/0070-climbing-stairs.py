class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [-1] * (n + 1)
        # def f(n):
        #     nonlocal dp
        #     if n in (0, 1, 2):
        #         dp[n] = n
        #         return n
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] =  f(n-1) + f(n-2)
        #     return dp[n]
        # return f(n)
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[ i-1] + dp[ i-2]
        return dp[n]
            
            