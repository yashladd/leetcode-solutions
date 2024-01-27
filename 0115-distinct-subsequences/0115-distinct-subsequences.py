class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        
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