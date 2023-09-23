class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            res = 0
            res += dp[i + 1]
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] < "7")):
                res += dp[i+2]
            dp[i] = res
            
        return dp[0]
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
            
        