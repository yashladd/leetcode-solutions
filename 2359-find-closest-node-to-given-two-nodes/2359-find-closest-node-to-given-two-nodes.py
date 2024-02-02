class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        g = defaultdict(list)
        for i, v in enumerate(edges):
            if v != -1:
                g[i].append(v)

        def bfs(node, dist):
            q = deque([node])
            dist[node] = 0
            while q:
                node = q.popleft()
                for nei in g[node]:
                    if dist[node] + 1 < dist[nei]:
                        dist[nei] = dist[node] + 1
                        q.append(nei)

        dist1 = [float("inf")] * n
        dist2 = [float("inf")] * n
        bfs(node1, dist1)
        bfs(node2, dist2)
        mini = float("inf")
        ans = -1
        # print(dist1)
        # print(dist2)
        for i in range(n):
            d1 = dist1[i]
            d2 = dist2[i]
            if d1 != float("inf") and d2 != float("inf"):
                if mini > max(d1, d2):
                    ans = i
                    mini = max(d1, d2)
        return ans
            

        