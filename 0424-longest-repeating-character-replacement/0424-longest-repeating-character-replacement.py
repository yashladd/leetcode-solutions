class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict(int)
        n = len(s)
        l, r = 0, 0
        maxi = 0
        while r < n:
            h[s[r]] += 1
            while r - l + 1 - max(h.values()) > k:
                h[s[l]] -= 1
                l += 1
            maxi = max(maxi, r-l+1)
            r += 1
        return maxi
            