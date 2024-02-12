class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, wt in roads:
            g[u].append((v, wt))
            g[v].append((u, wt))

        res = float("inf")
        dist = [float("inf")] * (n+1)
        h = []
        heappush(h, 1)
        while h:
            node = heappop(h)
            for nei, wt in g[node]:
                if wt < dist[nei] or dist[node] < dist[nei]:
                    dist[nei] = min(wt, dist[node])
                    heappush(h, nei)

        return dist[n]