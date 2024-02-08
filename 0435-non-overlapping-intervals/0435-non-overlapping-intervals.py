class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pe = intervals[0][1]
        cnt = 0
        for s, e in intervals[1:]:
            if s < pe:
                cnt += 1
                pe = min(e, pe)
            else:
                pe = e
        return cnt