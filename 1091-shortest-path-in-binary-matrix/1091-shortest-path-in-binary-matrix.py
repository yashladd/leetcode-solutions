class Solution:
    def shortestPathBinaryMatrix(self, g: List[List[int]]) -> int:
        N, M = len(g), len(g[0])
        INF = float("inf")
        dis = [[INF for _ in range(M)] for _ in range(N)]
        dis[0][0] = 0

        if g[0][0] or g[N-1][M-1]:
            return -1

        # vis = set()
        # vis.add((0, 0))
        DIRS = [
            (0,1), (1,0), (-1, 0), (0,-1),
            (1,1), (1,-1), (-1, 1), (-1,-1)
        ]

        def inb(i, j):
            return i >= 0 and j>=0 and i < N and j < M


        q = deque([(0, 0, 1)])

        while q:
            r, c, d = q.popleft()
            if r == N-1 and c == M-1:
                return d
            for dx, dy in DIRS:
                nr, nc = r + dx, c + dy
                if inb(nr, nc) and not g[nr][nc] and dis[nr][nc] > 1 + d:
                    dis[nr][nc] = 1 + d
                    q.append((nr, nc, 1 + d))

        return -1



        
        