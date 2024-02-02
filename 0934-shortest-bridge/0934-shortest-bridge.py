class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = [[0] * n for _ in range(n)]
        que = deque([])
        def addIsland(r,c):
            vis[r][c] = 1
            que.append((r,c))
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                p, q = r + dx, c + dy
                if p >= 0 and q >= 0 and p < n and q < n \
                        and not vis[p][q] and grid[p][q]:
                    addIsland(p, q)
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    addIsland(i, j)
                    found = True
                    break
            if found:
                break
        
        flips = 0
        while que:
            sz = len(que)
            for _ in range(sz):
                i, j = que.popleft()
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    p, q = i + dx, j + dy
                    if p >= 0 and q >= 0 and p < n and q < n and not vis[p][q]:
                        if grid[p][q] == 0:
                            vis[p][q] = 1
                            que.append((p, q))
                        else:
                            return flips
            flips += 1

        
        