class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        g = defaultdict(list)
        ind=[0 for _ in range(n)]
        for u, v in relations:
            g[u-1].append(v-1)
            ind[v-1] += 1

        @cache
        def dp(mask, deg):
            if not mask:
                return 0
            
            availableCourses = []
            # 11011
            for i in range(n):
                if mask & (1 << i) and deg[i] == 0:
                    availableCourses.append(i)
            ans = inf
            for choice in combinations(availableCourses, min(len(availableCourses), k)):
                newMask, newDeg = mask, list(deg)
                for course in choice:
                    newMask ^= (1 << course)
                    for nei in g[course]:
                        newDeg[nei] -= 1
                ans = min(ans, 1 + dp(newMask, tuple(newDeg)))
            return ans



        return dp((1 << n) - 1, tuple(ind))