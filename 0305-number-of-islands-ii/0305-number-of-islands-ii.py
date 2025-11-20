class DS:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # no merge happened
        # union by size
        if self.sz[rx] < self.sz[ry]:
            rx, ry = ry, rx
        self.p[ry] = rx
        self.sz[rx] += self.sz[ry]
        return True      # merged


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ds = DS(m * n)
        grid = [[0] * n for _ in range(m)]
        isl = 0
        res = []

        for i, j in positions:
            # ignore duplicate add-land operations
            if grid[i][j] == 1:
                res.append(isl)
                continue

            grid[i][j] = 1
            isl += 1
            idx = i * n + j

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                p, q = i + dx, j + dy
                if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                    nidx = p * n + q
                    if ds.union(idx, nidx):
                        isl -= 1  # only decrement when we really merged two islands

            res.append(isl)

        return res
