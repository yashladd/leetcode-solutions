class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @cache
        # def f(i, j):
        #     if i  < 0 or j < 0:
        #         return 0
        #     if text1[i] == text2[j]: return 1 + f(i-1, j-1)
        #     return max(f(i-1, j), f(i, j-1))
        # return f(len(text1)-1, len(text2)-1)
    
        n, m = len(text1), len(text2)
        dp = [ [0] * (m+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] =  max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]
                    
    