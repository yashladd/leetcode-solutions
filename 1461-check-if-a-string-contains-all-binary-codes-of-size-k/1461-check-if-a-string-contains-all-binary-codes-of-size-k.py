class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        h = {}
        for i in range(len(s)-k+1):
            curr = s[i:i+k]
            if curr in h:
                continue
            else:
                h[curr] = 1
        
        return len(h) == 2**k