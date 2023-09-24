class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1]*n
        def f(i):
            if i == n:
                return True
            if dp[i] != -1:
                return dp[i]
            
            j = i
            while j < n:
                if s[i:j+1] in wordDict:
                    if f(j+1):
                        dp[i] = True
                        return True
                j += 1
            dp[i] = False
            return False
        
        
        return f(0)