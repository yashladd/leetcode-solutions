class DS:
    def __init__(self, n):
        self.par = [0] * (n + 1)
        for i in range(n + 1):
            self.par[i] = i
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if node == self.par[node]:
            return node
        self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, u, v):
        up_u, up_v = self.find(u), self.find(v)
        if up_u == up_v:
            return 
        if self.size[up_u] < self.size[up_v]:
            self.par[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.par[up_v] = up_u
            self.size[up_u] += self.size[up_v]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ds = DS(n * m)
        
        def inb(x, y):
            return x >= 0 and x < n and y >= 0 and y < m
        
        vis = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not vis[i][j]:
                    vis[i][j] = 1
                    node = i * m + j
                    for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                        r, c = i + dx, j + dy
                        if inb(r, c)  and grid[r][c] and not vis[r][c]:
                            neigh = r * m + c
                            ds.union(node, neigh)
        
        maxi = max(ds.size)
        
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    size = 1
                    used = {}
                    for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
                        r, c = i + dx, j + dy
                        if inb(r, c)  and grid[r][c]:
                            node = r * m + c
                            parent = ds.find(node)
                            if parent not in used:
                                used[parent] = 1
                                size += ds.size[parent]
                    maxi = max(maxi, size)
                    
        return maxi
                                
        
        