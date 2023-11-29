class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m  = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        
        def f(i, j):
            vis[i][j] = 1
            num = 1
            q = deque([(i,j)])
            while q:
                i, j = q.popleft()
                for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if x >= 0 and y >= 0 and x < n and y < m and grid[x][y] == 1 \
                    and not vis[x][y]:
                        num += 1
                        q.append((x,y))
                        vis[x][y] = 1
            return num
                    
        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    maxi = max(maxi, f(i, j))
                    
                    
        return maxi