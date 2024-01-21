class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for sr, de in prerequisites:
            adj[sr].append(de)
            
        vis = [0] * numCourses
        path = [0] * numCourses

        def dfs(node):
            vis[node] = 1
            path[node] = 1
            for nei in adj[node]:
                if not vis[nei]:
                    if dfs(nei): return True
                elif path[nei]:
                    return True
            path[node] = 0  
            return False
        
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i): return False
                
        return True
                
                    
            
        