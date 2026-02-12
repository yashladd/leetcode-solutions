class Solution:
    def minDifficulty(self, jd: List[int], da: int) -> int:
        N = len(jd)

        dp = [[inf] * (da+1) for _ in range(N+1)]
        dp[N][0] = 0

        for i in range(N-1,-1,-1):
            for d in range(da+1):
                costToEndHere = jd[i] + dp[i+1][d-1]
                maxi = -inf
                for j in range(i, N):
                    maxi = max(maxi, jd[j])
                    costToEndHere = min(costToEndHere, maxi + dp[j+1][d-1])
                
                dp[i][d] = costToEndHere
        res = dp[0][da]  
        return res if res != inf else -1


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