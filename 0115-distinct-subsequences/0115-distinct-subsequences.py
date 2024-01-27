class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1+1):
            dp[i][l2] = 1
            
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
                    
        return dp[0][0]
        
        
        
        @cache
        def f(i, j):
            if j == l2:
                return 1
            if i == l1:
                return 0
            if s[i] == t[j]:
                return f(i+1, j+1) + f(i+1, j)
            else: 
                return f(i+1, j)
        
        return f(0, 0)