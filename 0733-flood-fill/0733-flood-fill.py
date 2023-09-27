class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        vis = [[False for i in range(m)] for _ in range(n)]
        col = [image[sr][sc]]
        res = copy.deepcopy(image)

        def inb(i, j):
            return i >= 0 and j >= 0 and i < n and j < m

        def bfs(i, j):
            nonlocal vis, col, res
            q = deque([(i, j)])

            while q:
                r, c = q.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dx, c + dy
                    if inb(nr, nc) and not vis[nr][nc] and image[nr][nc] == col[0]:
                        q.append((nr, nc))
                        res[nr][nc] = color
                        vis[nr][nc] = True

        vis[sr][sc] = True
        res[sr][sc] = color
        bfs(sr, sc)
        return res
            