class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        n, m = len(a), len(b)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(
                        dp[i+1][j],
                        dp[i][j+1]
                    )

        return dp[0][0]







        @cache
        def f(i, j):
            if i == n or j == m:
                return 0


            if a[i] == b[j]:
                return 1 + f(i+1, j+1)

            two = f(i+1, j)
            tre = f(i, j+1)

            return max(two, tre)

        return f(0, 0)


        