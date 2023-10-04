class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            lh, rh = height[l], height[r]
            a = (r-l) * min(lh, rh)
            res = max(a, res)
            if lh <= rh:
                l += 1
            else:
                r-=1
                
        return res
        