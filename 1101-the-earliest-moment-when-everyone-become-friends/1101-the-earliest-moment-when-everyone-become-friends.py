class DS:
    def __init__(self, n):
        self._p = [i for i in range(n+1)]
        self._s = [1 for _ in range(n+1)]

    def union(self, u, v):
        p_u, p_v = self.find(u), self.find(v)
        if p_u == p_v:
            return False
        
        if self._s[p_v] > self._s[p_u]:
            p_u, p_v = p_v, p_u

        self._p[p_v] = p_u
        self._s[p_u] += self._s[p_v]

        return True

    def find(self, u):
        p_u = self._p[u]
        if u == p_u:
            return u
        self._p[u] = self.find(self._p[u])
        return self._p[u]

    def getSize(self, u):
        return self._s[u]

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        ds = DS(n)

        for t, u, v in logs:
            res = ds.union(u, v)
            # print(ds._p)
            # print(ds._s)
            if res:
                u_s = ds.getSize(ds.find(u))
                v_s = ds.getSize(ds.find(v))

                if u_s == n or v_s == n:
                    return t

        return -1
        