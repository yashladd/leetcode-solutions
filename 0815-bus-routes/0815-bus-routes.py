class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        N = len(routes)
        g = defaultdict(list)
        if source == target: return 0

        for bus, stops in enumerate(routes):
            for stop in stops:
                g[stop].append(bus)

        vis = set()
        q = deque()
        for bus in g[source]:
            q.append((bus, 1))
            vis.add(bus)

        while q:
            s = len(q)
            for _ in range(s):
                bus, hops = q.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return hops

                    for bus in g[stop]:
                        if bus not in vis:
                            q.append((bus, hops + 1))
                            vis.add(bus)

        return -1


