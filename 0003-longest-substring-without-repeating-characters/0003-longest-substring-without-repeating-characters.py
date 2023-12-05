class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        lon = 0
        h = {}
        while r < n:
            if s[r] in h:
                l = max(h[s[r]] + 1, l)
                
            lon = max(lon, r - l + 1)
            h[s[r]] = r
            r += 1
            
        return lon
            
                
        