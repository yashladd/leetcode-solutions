class Solution:
    def minDeletions(self, s: str) -> int:
        f = Counter(s)

        seen = set()
        dels = 0
        for val in f.values():
            while val > 0 and val in seen:
                val -= 1
                dels += 1
            seen.add(val)

        return dels
