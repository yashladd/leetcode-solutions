from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        tf = Counter(t)
        req = len(tf)  # Number of unique characters in t to match
        mat = 0
        sf = Counter()
        
        l = 0
        min_l = inf
        min_s = ""
        
        for r, ch in enumerate(s):
            sf[ch] += 1
            if ch in tf and sf[ch] == tf[ch]:
                mat += 1
                
            while mat == req:
                if (r - l + 1) < min_l:
                    min_l = r - l + 1
                    min_s = s[l:r + 1]
                
                left_ch = s[l]
                sf[left_ch] -= 1
                if left_ch in tf and sf[left_ch] < tf[left_ch]:
                    mat -= 1
                l += 1
                
        return min_s