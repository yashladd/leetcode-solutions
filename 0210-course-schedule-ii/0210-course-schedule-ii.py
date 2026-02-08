class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        ind = [0] * numCourses

        for u, v in prereq:
            g[v].append(u)
            ind[u] += 1
        print(ind)
        q = deque([i for i in range(numCourses) if ind[i] == 0])
        topo = []
        print(q)
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in g[node]:
                ind[nei] -= 1
                if not ind[nei]:
                    q.append(nei)

        if len(topo) != numCourses:
            return []

        return topo

