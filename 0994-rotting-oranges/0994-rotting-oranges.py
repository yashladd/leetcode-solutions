class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        n, m = len(grid), len(grid[0])

        def inbound(i, j):
            return i >=0 and j >=0 and i < n and j < m

        vis = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    vis[i][j] = True

        mins = 0
        while q:
            siz = len(q)
            for _ in range(siz):
                r, c, t = q.popleft()
                mins = max(mins, t)
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    row, col = r + dx, c + dy
                    if inbound(row, col) and grid[row][col] in (1, 2)\
                     and not vis[row][col]:
                        q.append((row, col, t + 1))
                        grid[row][col] = 2
                        vis[row][col] = True


        if not all(element in (0, 2) for l in grid for element in l):
            return -1
        
        return mins 



        