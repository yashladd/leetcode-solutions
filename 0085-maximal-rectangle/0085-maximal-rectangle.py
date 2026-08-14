class Solution:
    def maximalRectangle(self, A: List[List[str]]) -> int:
        N, M = len(A), len(A[0])


        def lar_rec(arr):
            n = len(arr)

            stk = []
            maxi  =0
            for r, v in enumerate(arr):
                l = r
                while stk and stk[-1][0] > v:
                    ph, pi = stk.pop()
                    maxi = max(maxi, ph * (r - pi))
                    l = pi

                stk.append((v, l))

            while stk:
                ph, pi = stk.pop()
                maxi = max(maxi, ph * (n-pi))

            return maxi


        prev = list(map(int, A[0]))

        maxi = lar_rec(prev)

        for r in range(1, N):
            curr = [0] * M
            for c  in range(M):
                if A[r][c] == "1":
                    curr[c] = 1 + prev[c]

            maxi = max(maxi, lar_rec(curr))
            prev = curr

        return maxi
