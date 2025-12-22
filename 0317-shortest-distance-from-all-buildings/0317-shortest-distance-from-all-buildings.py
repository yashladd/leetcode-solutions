class Solution:
    def shortestDistance(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        distance = [[0] * m for _ in range(n)]
        reach = [[0] * m for _ in range(n)]
        buildings = 0 
        for r in range(n):
            for c in range(m):
                if g[r][c] == 1:
                    vis = set()

                    buildings += 1
                    q = deque([(r, c, 0)])
                    vis.add((r, c))
                    while q:
                        i, j, d = q.popleft()
                        for dx, dy in [(0,1), (1,0), (-1, 0), (0,-1)]:
                            x, y = i + dx, j + dy
                            if x >= 0 and y >= 0 and x < n and y < m and g[x][y] == 0 and (x,y) not in vis:
                                vis.add((x, y))
                                distance[x][y] += 1 + d
                                q.append((x, y, 1 + d))
                                reach[x][y] += 1

                    vis.clear()

        shortes = inf
        for i in range(n):
            for j in range(m):
                if reach[i][j] == buildings:
                    shortes = min(shortes, distance[i][j])

        return shortes if shortes != inf else -1
