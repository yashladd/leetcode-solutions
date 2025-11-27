class DS:
    def __init__(self, n):
        self.p = [i for i in range(n+1)]
        self.s = [1] * (n+1)

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, u, v):
        pU, pV = self.find(u), self.find(v)
        if pU == pV:
            return False
        if self.s[pU] < self.s[pV]:
            pU, pV = pV, pU

        self.p[pU] = pV
        self.s[pU] += self.s[pV]
        return True
        


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        g = defaultdict(list)

        comp = 0

        vis = set()
        ds = DS(n)

        extra = 0
        for u, v in connections:
            if not ds.union(u, v):
                extra += 1

        comps = 0
        for i in range(n):
            if i == ds.find(i):
                comps += 1

        if extra < comps - 1:
            return -1

        return comps - 1