class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        course_ordering = []

        frontier = deque()
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in relations:
            graph[u-1].append(v-1)
            indegree[v-1] += 1

        for i in range(n):
            if indegree[i] == 0:
                frontier.append(i)

        semesters = 0
        while frontier:
            next_frontier = deque()
            sz = len(frontier)

            for _ in range(sz):
                course = frontier.popleft()
                course_ordering.append(course)

                for next_course in graph[course]:
                    indegree[next_course] -= 1

                    if indegree[next_course] == 0:
                        next_frontier.append(next_course)

            frontier = next_frontier
            semesters += 1

        if len(course_ordering) != n:
            return -1

        return semesters 

        
            