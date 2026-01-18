class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        vals = set()
        for i, (u, v) in enumerate(equations):
            g[u].append((v, values[i]))
            g[v].append((u, 1/values[i]))
            vals.add(u)
            vals.add(v)

        def bfs(sr, de):
            found = False
            q = deque([(sr, 1.0)])
            vis = set()
            vis.add(sr)
            while q:
                node, cur = q.popleft()
                if node == de:
                    return cur
                for nei, mul in g[node]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append([nei, cur * mul])
            if not found:
                return -1.0
        res= []
        for u, v in queries:
            if u not in vals or v not in vals:
                res.append(-1)
                continue
            res.append(bfs(u, v))
        return res 


            

        