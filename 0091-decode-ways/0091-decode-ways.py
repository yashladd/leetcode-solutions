class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        chrs = [str(i) for i in range(1, 27)]
        dp = [-1] * n
        def f(idx):
            if idx == n:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            res = 0
            
            if s[idx] in chrs:
                res += f(idx+1)
            if idx + 2 <= n and s[idx: idx+2] in chrs:
                res += f(idx + 2)
            dp[idx] = res
            return res
        
        return f(0)
            
        