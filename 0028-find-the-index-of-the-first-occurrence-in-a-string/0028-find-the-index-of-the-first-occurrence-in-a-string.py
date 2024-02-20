class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        n, m = len(haystack), len(needle)
        lps = [0] * m
        prevLps, i = 0, 1
        # Precomputing LPS
        while i < m:
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                i += 1
                prevLps += 1
            elif prevLps == 0:
                lps[i] = 0                
                i += 1
            else:
                # We stay at the current index, perhaps some prefix matches this suffix
                prevLps = lps[prevLps-1]

        i, j = 0, 0
        while i < n:
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == m:
                return i - m
        return -1
