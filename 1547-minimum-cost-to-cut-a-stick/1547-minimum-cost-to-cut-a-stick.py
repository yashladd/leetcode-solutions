class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        N = len(cuts)
        cuts = [0] + cuts + [n]
        cuts.sort()
        dp = [[0]* (N+2) for _ in range(N+2)]

        for i in range(N, 0, -1):
            for j in range(1, N+1):
                if i > j:
                    continue
                mini = float("inf")
                for k in range(i, j+1):
                   
                    cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                    mini = min(mini, cost)
                dp[i][j] = mini
        return dp[1][N]



        def f(i, j):
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
           
            mini = float("inf")
            for k in range(i, j+1):
                cost = cuts[j+1] - cuts[i-1] + f(i, k-1) + f(k+1, j)
                mini = min(mini, cost)
            dp[i][j] = mini
            return mini

        return f(1, N)
        
