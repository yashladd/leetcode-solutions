class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)

    def union(self, u, v):
        p_u, p_v = self.find(u), self.find(v)
        if p_u == p_v:
            return 
        sz_u, sz_v = self.size[p_u], self.size[p_v]
        if sz_v > sz_u:
            p_v, p_u = p_u, p_v

        self.parent[p_v] = p_u
        self.size[p_u] += self.size[p_v]
        

    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ds = DisjointSet(26)

        equals = filter(lambda e: e[1] == "=", equations)
        not_equals = filter(lambda e: e[1] == "!", equations)

        for eq in equals:
            u = eq[0]
            v = eq[-1]
            u = ord(u) - ord('a')
            v = ord(v) - ord('a')
            ds.union(u, v)

        for eq in not_equals:
            u = eq[0]
            v = eq[-1]
            u = ord(u) - ord('a')
            v = ord(v) - ord('a')
            p_u, p_v = ds.find(u), ds.find(v)
            if p_u == p_v:
                return False
        return True
