class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        g = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            g[u].append(v)
            indegree[v] += 1

        q = deque()
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)
                visited.add(i)

        while q:
            node = q.popleft()

            for ch in g[node]:
                indegree[ch] -= 1
                if indegree[ch] == 0  and ch not in visited:
                    visited.add(ch)
                    q.append(ch)

        return len(visited) == numCourses


        