class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        path = [0] * n
        safe = [0] * n
        def dfs(node):
            vis[node] = 1
            path[node] = 1
            
            for nei in graph[node]:
                if not vis[nei]:
                    if dfs(nei):
                        return True
                elif path[nei]: 
                    return True
            safe[node] = 1   
            path[node] = 0
        
        for i in range(n):
            if not vis[i]:
                dfs(i)
                
        res = []
        for i in range(n):
            if safe[i]:
                res.append(i)
                
        return res
        
                
            
        