class DS:
    def __init__(self, n):
        self.par = [0] * (n+1)
        for i in range(n+1):
            self.par[i] = i
        self.size = [0] * (n + 1)
        
    def find(self, i):
        if i == self.par[i]:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]
    
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DS(n)
        
        for u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
            else:
                return [u, v]