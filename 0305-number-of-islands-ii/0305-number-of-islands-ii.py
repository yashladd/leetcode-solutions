class DS:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.size[pv] > self.size[pv]:
            pu, pv = pv, pu

        self.par[pv] = pu
        self.size[pu] += self.size[pv]
        return True

    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

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
