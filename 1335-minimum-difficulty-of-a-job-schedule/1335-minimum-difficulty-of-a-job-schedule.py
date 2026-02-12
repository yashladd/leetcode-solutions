class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        N = len(jd)
        @cache
        def f(i, d):
            if i == N:
                if d == 0:
                    return 0
                return inf

            if d <= 0:
                return inf

            costToEndHere = jd[i] + f(i+1, d-1)
            maxi = -inf
            for j in range(i, N):
                maxi = max(maxi, jd[j])
                costToEndHere = min(costToEndHere, maxi + f(j+1, d-1))
            return costToEndHere
        res = f(0, d)
        return res if res != inf else -1