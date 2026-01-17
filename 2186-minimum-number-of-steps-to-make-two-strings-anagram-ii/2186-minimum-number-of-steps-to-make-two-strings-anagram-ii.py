class Solution:
    def minSteps(self, s: str, t: str) -> int:

        return sum(list((Counter(s) - Counter(t)).values()) + list((Counter(t) - Counter(s)).values()))

        