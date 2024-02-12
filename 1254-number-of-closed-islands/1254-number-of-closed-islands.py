class Solution:
    def closedIsland(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        vis = [[0] * m for _ in range(n)]
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or g[i][j] or vis[i][j]:
                return 
            vis[i][j] = 1
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                x, y = i + dx, j + dy
                dfs(x, y)

        for i in range(n):
            if not g[i][0] and not vis[i][0]:
                dfs(i, 0)
            if not g[i][m-1] and not vis[i][m-1]:
                dfs(i, m-1)
        
        for j in range(m):
            if not g[0][j] and not vis[0][j]:
                dfs(0, j)
            if not g[n-1][j] and not vis[n-1][j]:
                dfs(n-1,j)
        isl = 0
        for i in range(n):
            for j in range(m):
                if not g[i][j] and not vis[i][j]:
                    isl += 1
                    dfs(i, j)
        return isl




        