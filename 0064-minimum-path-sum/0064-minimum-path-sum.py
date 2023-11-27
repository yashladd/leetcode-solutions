class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @cache
        def f(i, j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            if i >= n or j >= m:
                return float("inf") 
            return min(grid[i][j] + f(i+1,j) , grid[i][j] + f(i, j+1))
        return f(0, 0)
        