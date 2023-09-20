class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def f(n):
            nonlocal dp
            if n in (0, 1, 2):
                dp[n] = n
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] =  f(n-1) + f(n-2)
            return dp[n]
        
        f(n)
        # print(dp)
        return dp[n]
            
            