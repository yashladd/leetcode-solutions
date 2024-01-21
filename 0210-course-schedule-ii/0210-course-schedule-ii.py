class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for sr, de in prerequisites:
            adj[de].append(sr)
        stk = []
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
            stk.append(node)
            return False
        
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i): return []
                
        return stk[::-1]
                
                    
            
        