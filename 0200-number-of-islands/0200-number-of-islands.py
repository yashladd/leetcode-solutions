class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])
        vis  = [[0 for _ in range(n)] for _ in range(m)]
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < m and j < n

        def bfs(i, j):
            vis[i][j] = 1
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newR, newC = r + dx, c + dy
                    if inbound(newR, newC) and grid[newR][newC] == "1" \
                    and vis[newR][newC] == 0:
                        q.append((newR, newC))
                        vis[newR][newC] = 1


        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if vis[i][j] == 0:
                        islands += 1
                        bfs(i, j)

        return islands