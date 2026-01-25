class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # n = len(relations)
        g = defaultdict(list)
        indeg = [0 for _ in range(n)]

        for u, v in relations:
            g[u-1].append(v-1)
            indeg[v-1] += 1

        q = deque()
        maxi=0
        prevMaxTimes = [0 for _ in range(n)]
        for i in range(n):
            if not indeg[i]:
                q.append((i))
                prevMaxTimes[i] = 0

        while q:
            node = q.popleft()
            maxi = max(maxi, prevMaxTimes[node] + time[node])
            for nei in g[node]:
                indeg[nei] -= 1
                prevMaxTimes[nei] = max(prevMaxTimes[nei], prevMaxTimes[node] + time[node])
                if not indeg[nei]:
                    q.append((nei))

        return maxi


            



        