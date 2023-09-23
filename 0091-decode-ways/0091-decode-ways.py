class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def f(idx):
            if idx == n:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            if s[idx] == "0":
                dp[idx] = 0
                return 0
            
            res = 0
            res += f(idx+1)
            if idx + 1 < n and (s[idx] == "1" or (s[idx] == "2" and s[idx + 1] < "7")):
                res += f(idx + 2)
            dp[idx] = res
            return res
        
        return f(0)
            
        