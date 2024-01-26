class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        G = defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    wt = abs(x1-x2) + abs(y1-y2)
                    G[i].append((j, wt))
                    G[j].append((i, wt))
        
        minCost = 0
        vis = set()
        
        h = []
        heappush(h, (0, 0))
        
        while h:
            wt, node = heappop(h)
            if node in vis: continue
            vis.add(node)
            minCost += wt
            for nei, wt in G[node]:
                if nei not in vis:
                    heappush(h, (wt, nei))
                    
        return minCost