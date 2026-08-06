from enum import IntEnum
class State(IntEnum):
    COMPLETED = 1
    VISITING = 2

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for u, c in prerequisites:
            g[u].append(c)

        state = {}
        res = []
        for course in range(numCourses):
            if course not in state:
                if self.visit_dependencies_and_check_cycle(g, course, state, res):
                    return []

        return res
    

    def visit_dependencies_and_check_cycle(self, g, course, state, res):
        s = state.get(course)
        if s == State.COMPLETED: return False
        if s == State.VISITING:  return True

        state[course] = State.VISITING

        for dep in g[course]:
            if self.visit_dependencies_and_check_cycle(g, dep, state, res):
                return True

        res.append(course)
        state[course] = State.COMPLETED
        return False
        