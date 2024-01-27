class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vis = [0] * (n+1)
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))
    
        h = []
        heappush(h, (0, k))
        visCnt = 1
        dist = [float("inf")] * (n+1)
        dist[k] = 0
        while h:
            time, node = heappop(h)
            for nei, wt in g[node]:
                nextTime = time + wt
                if nextTime < dist[nei]:
                    dist[nei] = nextTime
                    visCnt += 1
                    heappush(h, (nextTime, nei))
        # print(visCnt, dist)            
        return -1 if visCnt < n else max(dist[1:])
                    