class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 0
        
        # 1. Precompute all palindromes in O(N^2)
        # is_pal[i][j] will be True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2 or is_pal[i+1][j-1]:
                        is_pal[i][j] = True
        
        # 2. DP to find min cuts
        # dp[i] is the min cuts for prefix s[0...i]
        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                # Initialize with maximum possible cuts (each char is a cut)
                dp[i] = i 
                for j in range(i):
                    if is_pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
                        
        return dp[n - 1]