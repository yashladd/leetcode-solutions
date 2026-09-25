class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        COMPLETED = 1
        VISITING = 2


        visit_status = {}


        g = defaultdict(list)


        for u, v in prerequisites:
            g[v].append(u)


        def dfs(node):
            visit_status[node] = VISITING

            for ch in g[node]:
                if ch in visit_status:
                    if visit_status[ch] == VISITING:
                        return True
                elif dfs(ch):
                    return True

            visit_status[node] = COMPLETED

            return False

        
        for i in range(numCourses):
            if i not in visit_status or visit_status[i] != COMPLETED:
                if dfs(i):
                    return False

        return True


        