class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        r = defaultdict(set)
        b = defaultdict(set)
        for u, v in redEdges:
            r[u].add(v)    
        for u, v in blueEdges:
            b[u].add(v)
        q = deque([])
        q.append((0, 0, -1))
        dist = [float("inf")] * n
        dist[0] = 0

        while q:
            d, node, prev = q.popleft()
            if prev != 1:
                for nei in b[node].copy():
                    curr = d + 1
                    if curr < dist[nei]:
                        dist[nei] = curr
                    b[node].discard(nei)
                    q.append((curr, nei, 1))
            
            if prev != 0:
                for nei in r[node].copy():
                    curr = d + 1
                    if curr < dist[nei]:
                        dist[nei] = curr
                    r[node].discard(nei)
                    q.append((curr, nei, 0))
                        
        dist = [x if x != float("inf") else -1 for x in dist]
        return dist
                    
            
        