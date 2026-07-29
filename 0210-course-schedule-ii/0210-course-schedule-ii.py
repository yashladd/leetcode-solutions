class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        topo = []

        g = defaultdict(list)
        ind = [0] * numCourses
        for u, v in prerequisites:
            g[v].append(u)
            ind[u] += 1
        q = deque()
        for i in range(numCourses):
            if not ind[i]:
                q.append(i)

        while q:
            node  = q.popleft()
            topo.append(node)
            for ch in g[node]:
                ind[ch] -= 1
                if ind[ch] == 0:
                    q.append(ch)

        if len(topo) != numCourses:
            return []

        return topo
