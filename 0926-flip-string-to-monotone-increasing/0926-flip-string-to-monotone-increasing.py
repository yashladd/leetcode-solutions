class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        ones = 0

        for n in s:
            if n == "1":
                ones += 1
            else:
                flips = min(flips + 1, ones)
        return flips