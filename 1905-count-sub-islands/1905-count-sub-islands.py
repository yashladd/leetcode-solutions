class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        vis = [[0] * m for _ in range(n)]
        
        def inb(i,j):
            return i >= 0 and i < n and j >= 0 and j < m
        
        def dfs(i, j):
            vis[i][j] = 1
            ret = True
            if grid1[i][j] == 0:
                ret = False
            
            for dx, dy in [(0,1), (1, 0), (0,-1), (-1, 0)]:
                r, c = i + dx, j + dy
                if inb(r,c) and not vis[r][c] and grid2[r][c] == 1:
                    if not dfs(r, c):
                        ret = False
                    
            return ret
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid2[i][j] == 1:
                    if dfs(i, j):
                        print(i, j)
                        cnt += 1
                        
        return cnt
                
            
        