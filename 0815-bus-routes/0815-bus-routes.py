class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)


        for i, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(i)

        vis = set()
        q = deque()
        for bus in stop_to_buses[source]:
            q.append(bus)
            vis.add(bus)

        num_buses = 1

        while q:
            sz = len(q)

            for _ in range(sz):
                bus_no = q.popleft()

                for stop in routes[bus_no]:
                    if stop == target:
                        return num_buses

                    for bus in stop_to_buses[stop]:
                        if bus not in vis:
                            q.append(bus)
                            vis.add(bus)

            num_buses += 1

        return -1
                