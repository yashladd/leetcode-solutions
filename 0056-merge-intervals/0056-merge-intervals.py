class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort()
        res = [ ]

        cur = i[0]
        res = [cur]
        for s, e in i[1:]:
            cs, ce = res[-1]
            if s <= ce:
                res[-1][1] = max(e, ce)
            else:
                res.append([s,e])
        return res