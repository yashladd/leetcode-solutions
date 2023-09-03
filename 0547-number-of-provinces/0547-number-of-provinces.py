class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = {}
        n = len(isConnected)
        adj = [ [] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        def dfs(node):
            vis[node] = 1
            
            for ne in adj[node]:
                if ne not in vis:
                    dfs(ne)
        
        provinces = 0
        for i in range(n):
            if i not in vis:
                provinces += 1
                dfs(i)
                
        return provinces
            
            