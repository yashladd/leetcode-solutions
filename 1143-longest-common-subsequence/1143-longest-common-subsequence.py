class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def f(i, j):
            if i  < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]: return 1 + f(i-1, j-1)
            
            return max(f(i-1, j), f(i, j-1))
        return f(len(text1)-1, len(text2)-1)