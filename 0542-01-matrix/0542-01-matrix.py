class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        res = copy.deepcopy(mat)
        q = deque([])
        vis = {}
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    vis[(i, j)] = 1
        def inb(i, j):
            return i >= 0 and j >= 0 and i < n and j < m
        while q:
            z = len(q)
            for _ in range(z):
                i, j, t = q.popleft()
                for dx, dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + dx, j + dy
                    if inb(r, c) and (r, c) not in vis and mat[r][c] == 1:
                        res[r][c] = t + 1
                        q.append((r, c, t + 1))
                        vis[(r, c)] = 1

        return res

        