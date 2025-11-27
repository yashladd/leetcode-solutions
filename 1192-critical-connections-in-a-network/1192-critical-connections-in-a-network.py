class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        time = [0]
        low = [0] * n
        tin = [0] * n
        vis = set()
        res = []

        def d(no, pa):
            tin[no] = low[no] = time[0]
            time[0] += 1
            vis.add(no)
            for ne in g[no]:
                if ne == pa:
                    continue
                if ne not in vis:
                    d(ne, no)
                if low[ne] > tin[no]:
                    res.append([no, ne])
                low[no] = min(low[ne], low[no])

        d(0, -1)
        return res


        