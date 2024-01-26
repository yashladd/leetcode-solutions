class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        G = defaultdict(list)
        for par, child in connections:
            G[par].append((child, 1))
            G[child].append((par, 0))
            
        q = deque([0])
        vis = set()
        cnt = 0
        vis.add(0)
        while q:
            node = q.popleft()
            for nei, cost in G[node]:
                if nei not in vis:
                    vis.add(node)
                    cnt += cost
                    q.append(nei)

        return cnt
        