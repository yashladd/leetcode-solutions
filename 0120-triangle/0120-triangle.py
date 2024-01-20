class Solution:
    def minimumTotal(self, a: List[List[int]]) -> int:
        n = len(a)
        dp = a[-1][:]
        # print(dp)
            
        for i in range(n-2, -1, -1):
            curr = [0] * (len(a[i]))
            for j in range(len(a[i])):
                curr[j] = min(a[i][j] + dp[j], a[i][j] + dp[j+1])
            dp = curr
                
        return dp[0]
        
        @cache
        def f(i, j):
            if i == n-1:
                return a[n-1][j]
            
            return min(a[i][j] + f(i+1, j), a[i][j] + f(i+1, j+1))
        
        return f(0, 0)
            
            
        