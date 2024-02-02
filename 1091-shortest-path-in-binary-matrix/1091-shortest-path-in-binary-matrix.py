class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        vis = [[0] * n for _ in range(n)]
        vis[0][0] = 1
        while q:
            sz = len(q)
            print(q)
            for _ in range(sz):
                i, j, l = q.popleft()
                if i == n-1 and j == n-1:
                    return l
                for dx, dy in [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,-1], [-1,1]]:
                    r, c = i + dx, j + dy
                    if (r >= 0 and c >= 0 and r < n and c < n) and not vis[r][c] and not grid[r][c]:
                        vis[r][c] = 1
                        q.append((r, c, l + 1))

        return -1


                
                
        
        
        