class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        idx = 0
        secrets = set()
        secrets.add(0)
        secrets.add(firstPerson)
        events = {}
        for u, v, t in meetings:
            if t not in events:
                events[t] = defaultdict(list)
            events[t][u].append(v)
            events[t][v].append(u)
        for t in sorted(events.keys()):
            q = deque([])
            g = events[t]
            vis = set()
            for event in g.keys():
                if event in secrets:
                    q.append(event)
                    vis.add(event)
            while q:
                node = q.popleft()
                for nei in g[node]:
                    if nei not in vis:
                        secrets.add(nei)
                        vis.add(nei)
                        q.append(nei)
        return list(secrets)