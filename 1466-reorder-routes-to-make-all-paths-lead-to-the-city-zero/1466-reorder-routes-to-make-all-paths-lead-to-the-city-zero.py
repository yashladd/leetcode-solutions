class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(x, y) for x, y in connections}
        G = defaultdict(list)
        for par, child in connections:
            G[par].append(child)
            G[child].append(par)
            
        reverse = 0
        vis = {}
        def dfs(node):
            nonlocal reverse
            vis[node] = 1
            for nei in G[node]:
                if nei not in vis:
                    if (nei, node) not in edges:
                        reverse += 1
                    dfs(nei)
        dfs(0)
        return reverse
        