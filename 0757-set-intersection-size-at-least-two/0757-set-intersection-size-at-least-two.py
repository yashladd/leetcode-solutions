class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key = lambda x: (x[1], -x[0]))

        p1, p2 = -1, -1

        for a, b in intervals:
            if p2  < a:
                res += 2
                p1, p2 = b-1, b
            elif p1 < a:
                res += 1
                p1, p2 = p2, b

        return res

        