class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, wt in roads:
            g[u].append((v, wt))
            g[v].append((u, wt))

        res = float("inf")
        vis = [0] * (n+1)
        
        def dfs(node):
            nonlocal res
            if not vis[node]:
                vis[node] = 1
                for nei, wt in g[node]:
                    res = min(res, wt)
                    dfs(nei)
        dfs(1)
        return res