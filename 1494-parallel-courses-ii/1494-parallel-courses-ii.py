class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """

        0000

        """
        g = defaultdict(list)
        indeg = [0 for _ in range(n)]

        for u, v in relations:
            g[u-1].append(v-1)
            indeg[v-1] += 1

        @cache
        def rec(mask, indeg):
            if not mask:
                return 0

            availCourses = [i for i in range(n) if mask & (1 << i) and not indeg[i]]
            ans = float("inf")
            for courses in combinations(availCourses, min(len(availCourses), k)):
                newMask, newIndg = mask, list(indeg)
                for node in courses:
                    newMask ^= (1 << node)
                    for nei in g[node]:
                        newIndg[nei] -= 1
                ans = min(ans, 1 + rec(newMask, tuple(newIndg)))

            return ans
            
            
        
        return rec((1 << n) - 1, tuple(indeg))

