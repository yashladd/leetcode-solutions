class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if (i < 0 or j < 0 or i >= n or j >= m  
                or grid[i][j] == 0):
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            maxi = 0
            maxi = max(
                dfs(i+1, j),
                dfs(i-1, j),
                dfs(i, j-1),
                dfs(i, j+1)
            )
            grid[i][j] = val
            return val + maxi

        
        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxi = max(maxi, dfs(i, j))

        return maxi


        