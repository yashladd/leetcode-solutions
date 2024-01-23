class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        
        G = defaultdict(set)
        for u, v in connections:
            G[u].add(v)
            G[v].add(u)
            
        vis = {}
        def dfs(node):
            vis[node] = 1
            for nei in G[node]:
                if nei not in vis:
                    dfs(nei)
                    
        comp = 0
        for i in range(n):
            if i not in vis:
                dfs(i)
                comp += 1
                
        return comp - 1
        