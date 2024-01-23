class Ds:
    def __init__(self, n):
        self.n = n
        self.parent = [0] * (self.n + 1)
        self.size = [1] * (self.n + 1)
        for i in range(n+1):
            self.parent[i] = i
            
    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        up_u, up_v = self.findUParent(u), self.findUParent(v)
        if up_u == up_v:
            return 
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]
                
            
            

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = Ds(n)
        extraEdges = 0
        for u, v in connections:
            if ds.findUParent(u) == ds.findUParent(v):
                extraEdges += 1
                continue
            else:
                ds.unionBySize(u, v)
        
        numComponents = 0
        for i in range(n):
            if i == ds.parent[i]:
                numComponents += 1
                
        return numComponents - 1 if extraEdges >= numComponents - 1 else -1
            
            
        