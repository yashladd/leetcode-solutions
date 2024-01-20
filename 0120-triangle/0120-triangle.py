class Solution:
    def minimumTotal(self, a: List[List[int]]) -> int:
        n = len(a)
        dp = [[0] * (len(a[-1])) for _ in range(n)]
        for j in range(len(dp[-1])):
            dp[n-1][j] = a[n-1][j]
            
        for i in range(n-2, -1, -1):
            for j in range(len(a[i])):
                dp[i][j] = min(a[i][j] + dp[i+1][j], a[i][j] + dp[i+1][j+1])
                
        return dp[0][0]
        
        @cache
        def f(i, j):
            if i == n-1:
                return a[n-1][j]
            
            return min(a[i][j] + f(i+1, j), a[i][j] + f(i+1, j+1))
        
        return f(0, 0)
            
            
        