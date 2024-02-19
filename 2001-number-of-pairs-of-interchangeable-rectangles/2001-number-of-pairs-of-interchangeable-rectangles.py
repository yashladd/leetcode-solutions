class Solution:
    def interchangeableRectangles(self, r: List[List[int]]) -> int:
        m = defaultdict(int)
        res = 0
        for w,h in r:
            ratio = w/h
            if ratio in m:
                res += m[ratio]
            m[ratio] += 1
        return res
        
