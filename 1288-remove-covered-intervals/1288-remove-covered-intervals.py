class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key = lambda x: (x[0], -x[1]))
        uncovered = [intervals[0]]
        for i in range(1, N):
            a, b = intervals[i]
            c, d = uncovered[-1]

            if c <= a and b <= d:
                continue
            uncovered.append([a,b])

        return len(uncovered)
