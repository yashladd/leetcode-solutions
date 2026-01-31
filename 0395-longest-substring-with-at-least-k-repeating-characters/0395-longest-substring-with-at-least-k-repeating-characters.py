from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUniqueChars = len(set(s))
        best = 0

        for uniqueChars in range(1, maxUniqueChars + 1):
            freq = defaultdict(int)
            countAtLeastK = 0
            l = 0

            for r in range(len(s)):
                # expand window
                freq[s[r]] += 1
                if freq[s[r]] == k:
                    countAtLeastK += 1

                # shrink if too many unique chars
                while len(freq) > uniqueChars:
                    if freq[s[l]] == k:
                        countAtLeastK -= 1
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        del freq[s[l]]
                    l += 1

                # O(1) validity check
                if  countAtLeastK == uniqueChars:
                    best = max(best, r - l + 1)

        return best
