class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m  = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        
        def f(i, j):
            vis[i][j] = 1
            
            for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                x, y = i + dx, j + dy
                if x >= 0 and y >= 0 and x < n and y < m and grid[x][y] == "1" and not vis[x][y]:
                    f(x, y)
                    
        
        num = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not vis[i][j]:
                    num += 1
                    f(i, j)
                    
                    
        return num
                    
        