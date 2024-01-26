class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        G = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            G[i][i] = 0
            
        for u, v in prerequisites:
            G[u][v] = 1
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])
                    
        ans = [False] * len(queries)
        
        for i, (u, v) in enumerate(queries):
            if G[u][v] != float("inf"):
                ans[i] = True
                
        return ans
            
        
        
        