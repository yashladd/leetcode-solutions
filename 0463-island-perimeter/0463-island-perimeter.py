class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        vis = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 1
            if (i,j) in vis:
                return 0
            vis.add((i, j))
            peri = 0
            peri += dfs(i+1,j)
            peri += dfs(i,j+1)
            peri += dfs(i-1,j)
            peri += dfs(i,j-1)
            return peri
            
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)
        