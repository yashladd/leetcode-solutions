class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = []
        heappush(h, ( grid[0][0], (0, 0)))
        
        def inb(i, j):
            return i >= 0 and j >= 0 and i < n and j < n
        
        vis = [[float("inf")] * n for _ in range(n)]
        vis[0][0] = grid[0][0]
        while h:
            time, (r, c) = heappop(h)
            if r == n-1 and c == n-1:
                return time
            # if vis[r][c]:
            #     continue
            # vis[r][c] = 1
            for dx, dy in [(0,1), (1, 0), (0,-1), (-1, 0)]:
                x, y = r + dx, c + dy
                
                if inb(x,y):
                    newTime = max(grid[x][y], time)
                    if newTime < vis[x][y]:
                        vis[x][y] = newTime
                        heappush(h, (newTime, (x, y)))
                            
        