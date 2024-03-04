class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)
        orig = s * 2
        p, q = "01" * N, "10" * N
        best = 0
        d1 = d2 =  0

        for i in range(N):
            if orig[i] != p[i]:
                d1 += 1
            if orig[i] != q[i]:
                d2 += 1
        best = min(d1, d2)
        if not best: return best
        for j in range(N, 2*N):
            if p[j] != orig[j]:
                d1 += 1
            if p[j-N] != orig[j-N]:
                d1 -= 1
            if q[j] != orig[j]:
                d2 += 1
            if q[j-N] != orig[j-N]:
                d2 -= 1
            best = min([best, d1, d2])

        return best