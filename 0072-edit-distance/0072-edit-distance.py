class Solution:
    def minDistance(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        # @cache
        # def f(i, j):
        #     if j < 0 or i < 0:
        #         return max(i, j) + 1

        #     if s[i] == t[j]: return f(i-1, j-1)
            
        #     insert = 1 + f(i,j-1)

        #     delete = 1 + f(i-1, j)

        #     replace = 1 + f(i-1, j-1)

        #     return min(insert, delete, replace)

        # return f(n-1, m-1)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i

        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue

                insert = 1 + dp[i][j-1]

                delete = 1 + dp[i-1][j]

                replace = 1 + dp[i-1][j-1]

                dp[i][j] = min(insert, delete, replace)

        return dp[n][m]