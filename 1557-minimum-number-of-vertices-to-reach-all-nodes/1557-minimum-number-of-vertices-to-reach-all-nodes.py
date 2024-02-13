class DS:
    def __init__(self, n):
        self.par = [1] * (n)
        for i in range(n):
            self.par[i] = i
        self.size = [1] * n
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ind=[0] * n
        for u, v in edges:
            ind[v] += 1
        res = []
        for i in range(n):
            if not ind[i]:
                res.append(i)
        return res
        