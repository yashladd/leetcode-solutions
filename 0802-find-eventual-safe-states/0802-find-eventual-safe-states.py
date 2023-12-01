class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        v = [0] * n
        p = [0] * n
        c= [0] * n
        
        def dfs(node):
            v[node] = 1
            p[node] = 1
            
            for nei in graph[node]:
                if not v[nei]:
                    if dfs(nei):
                        c[node] = 0
                        return True
                elif p[nei]:
                    c[node] = 0
                    return True
                
            c[node] = 1
            p[node] = 0
            
            return False
        
        for i in range(n):
            if not v[i]:
                dfs(i)
                
                
        res = []
        for i in range(n):
            if c[i]:
                res.append(i)
        
        return res
                
                    
            
        