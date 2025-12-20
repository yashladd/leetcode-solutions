class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsToMerge = sorted(intervals, key = lambda x: x[0])
        res = [intervalsToMerge[0]]

        for start, end in intervalsToMerge[1:]:
            print(start, end, res)
            if res[-1][-1] >= start:
                res[-1][-1] = max(res[-1][-1], end)
            else:
                res.append([start,end])

        return res
        