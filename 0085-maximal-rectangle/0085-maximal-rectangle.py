class Solution:
    def maximalRectangle(self, a: List[List[str]]) -> int:
        h = list(map(int, a[0]))
        n, m = len(a), len(a[0])
        res = self.largest(h)
        for r in range(1, n):
            for c in range(m):
                h[c] = h[c] + 1 if a[r][c] == "1" else 0
            res = max(res, self.largest(h))

        return res

    def largest(self, a):
        n = len(a)
        stk = []
        res = 0
        for r in range(n):
            l = r
            while stk and stk[-1][1] > a[r]:
                l, ph = stk.pop()
                res = max(res, (r-l) * ph)
            stk.append((l, a[r]))

        while stk:
            l, h = stk.pop()
            res = max(res, (n-l) * h)

        return res 