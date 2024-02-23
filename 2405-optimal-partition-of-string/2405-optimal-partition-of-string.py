class Solution:
    def partitionString(self, s: str) -> int:
        parts = 0
        n = len(s)
        i = 0
        while i < n:
            parts += 1
            h = {s[i]: 1}
            while i+1 < n and s[i + 1] not in h:
                i += 1
                h[s[i]] = 1
            i += 1
        return parts
        