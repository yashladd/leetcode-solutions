class Solution:
    def strStr(self, s: str, p: str) -> int:
        if p == "": return 0

        n, m = len(s), len(p)
        
        i, j = 0, 0

        for i in range(n-m+1):
            if s[i: i+m] == p:
                return i

        return -1
            
