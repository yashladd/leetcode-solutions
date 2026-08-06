from enum import IntEnum
class State(IntEnum):
    COMPLETED = 1
    VISITED = 2
    PATH_VISITED = 3

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        GRAY, BLACK = 1, 2
        state = {}
        out = []

        # build adjacency: course -> list of courses it depends on (must take first)
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:        # must take b before a  →  edge a -> b
            adj[a].append(b)

        def dfs(c):
            if state.get(c) == BLACK:
                return True
            if state.get(c) == GRAY:      # on current path → back edge → cycle
                return False
            state[c] = GRAY
            for dep in adj[c]:
                if not dfs(dep):
                    return False
            state[c] = BLACK
            out.append(c)                 # post-order: append after deps
            return True

        for c in range(numCourses):
            if c not in state:
                if not dfs(c):
                    return []
        return out