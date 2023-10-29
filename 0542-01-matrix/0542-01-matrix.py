class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        vis = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[i][j] = 1
                
        dist = [[0] * m for _ in range(n)]
        while q:
                r, c, step = q.popleft()
                dist[r][c] = step
                for dx, dy in [(0,1), (1,0), (-1, 0), (0, -1)]:
                    x, y = r + dx, c + dy
                    if x >= 0 and y >= 0 and x < n and y < m:
                        if not vis[x][y]:
                            q.append((x, y, step + 1))
                            vis[x][y] = 1
                        
        return dist
    
    