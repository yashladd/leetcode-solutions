class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(list)
        ind = [0] * n
        for u, v in prerequisites:
            g[u].append(v)
            ind[v] += 1
        
        q = deque([])
        for i in range(n):
            if not ind[i]: 
                q.append(i)
        
        reach = [[False] * n for _ in range(n)]
        
        while q:
            node = q.popleft()
            for nei in g[node]:
                reach[node][nei] = True
                
                for i in range(n):
                    if reach[i][node]:
                        reach[i][nei] = True
                        
                ind[nei] -= 1
                if not ind[nei]:
                    q.append(nei)
                    
                    
        return [reach[u][v] for u, v in queries]
                
            
        
        
        