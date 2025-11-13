class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        i = 0
        res = 0
        n = len(s)
        while i < len(s):
            if s[i] == "0":
                while i + 1 < n and s[i+1] == "0":
                    i += 1
                res += ones
            else:
                ones += 1
            i += 1
        
        return res
