class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                g[v].append(i)
        
        maxi = [-float("inf")]
        def f(node, time):
            curr = 0
            for nei in g[node]:
                f(nei, time + informTime[node])
            maxi[0] = max(maxi[0], time)
        
        f(headID, 0)
        
        return maxi[0]