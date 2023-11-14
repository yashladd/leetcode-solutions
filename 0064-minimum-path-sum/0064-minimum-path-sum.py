class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-1] * m for _ in range(n)]
        def f(i, j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            if i >= n or j >= m:
                return float("inf") 
            if dp[i][j] !=-1 : return dp[i][j]
            dp[i][j] = min(grid[i][j] + f(i+1,j) , grid[i][j] + f(i, j+1))
            return dp[i][j]
        a =  f(0, 0)
        # print(a)x
        return a
        