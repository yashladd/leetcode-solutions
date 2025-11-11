class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        @lru_cache(None)
        def f(i, j):
            if i < 0 or j < 0:
                if j >= 0 and p[j] == "*":
                    return f(i, j-1)
                return i == j

            if s[i] == p[j] or p[j] == "?":
                return f(i-1, j-1)

            if p[j] == "*":
                return f(i-1, j) or f(i, j-1)

            return False

        return f(n-1, m-1)