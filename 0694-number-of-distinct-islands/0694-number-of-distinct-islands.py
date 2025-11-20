class Solution:
    def inbound(self, i, j, n, m):
        return i >= 0 and j >= 0 and i < n and j < m
        
    def dfs(self, i, j, vis, g, ds, base):
        vis[i][j] = 1
        bsx, bsy = base
        ds.append((i - bsx, j - bsy))
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            x, y = i + dx, j + dy
            if self.inbound(x, y, len(g), len(g[0])) and g[x][y] == 1 and not vis[x][y] :
                self.dfs(x, y, vis, g, ds, base)
        
        
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # code here
        n, m = len(grid), len(grid[0])
        s = set()
        vis = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == 1:
                    lis = []
                    self.dfs(i, j, vis, grid, lis, (i, j))
                    # print(lis)
                    s.add(tuple(lis))
                    # print(s)
                    
        return len(s)


