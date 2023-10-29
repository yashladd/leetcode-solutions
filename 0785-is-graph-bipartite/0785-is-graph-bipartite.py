class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1] * n
        
        def bfs(node):
            col[node] = 0
            q = deque([node])
            
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if col[nei] == -1:
                        col[nei] = col[curr] ^ 1
                        q.append(nei)
                    elif col[curr] == col[nei]:
                        return True
            return False
        
        for i in range(n):
            if col[i] == -1:
                if bfs(i):
                    return False
                
        return True
        