class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        lon = 0
        seen = set()
        while r < n:
            if s[r] in seen:
                while s[r] in seen:
                    seen.discard(s[l])
                    l += 1
            seen.add(s[r])
            lon = max(lon, r-l+1)
            r += 1
        return lon
            
                
        