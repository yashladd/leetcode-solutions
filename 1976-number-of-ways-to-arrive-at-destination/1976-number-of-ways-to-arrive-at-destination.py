class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for sr, de, wt in roads:
            adj[sr].append((de, wt))
            adj[de].append((sr, wt))
            
        dist = [float("inf")] * n
        ways = [0] * n
        ways[0] = 1
        dist[0] = 0
        h = []
        heappush(h, (0, 0))
        while h:
            time, node = heappop(h)
            for nei, wt in adj[node]:
                newTime = time + wt
                if newTime < dist[nei]:
                    dist[nei] = newTime
                    ways[nei] = ways[node]
                    heappush(h, (newTime, nei))
                elif newTime == dist[nei]:
                    ways[nei] = int((ways[nei] + ways[node]) % (1e9 + 7))
                        
        return int(ways[-1] % (1e9 + 7))
            
        