class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        a   a
        a * a
        """
        @cache
        def f(i, j):
            if i < 0 or j < 0:
                if i < 0:

                    if j < 0:
                        return True
                    if p[j] == "*":
                        return f(i, j-1)
                return False

            if s[i] == p[j] or p[j] == "?": return f(i-1, j-1)

            if p[j] == "*":
                return f(i-1, j) or f(i, j-1)
            return False

        n, m = len(s), len(p)
        return f(n-1, m-1)
        