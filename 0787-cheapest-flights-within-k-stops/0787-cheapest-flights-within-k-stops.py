class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        path = [float("inf")] * n
        adj = defaultdict(list)
        for sr, de, wt in flights:
            adj[sr].append((de, wt))
        path[src] = 0
        q = []
        heappush(q, (0, 0, src))
        
        while q:
            stops, dist, node = heappop(q)
            if stops > k: continue
            for nei, wt in adj[node]:
                potD = dist + wt
                if potD < path[nei]:
                    heappush(q, (stops + 1, potD, nei))
                    path[nei] = potD
        
        return -1 if path[dst] == float("inf") else path[dst]
                    
            