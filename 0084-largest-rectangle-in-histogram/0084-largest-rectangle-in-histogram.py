class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = -float("inf")
        stk = []
        for i, h in enumerate(heights):
            prevIdx = i
            while stk and stk[-1][1] > h:
                prevIdx, prevHeight = stk.pop()
                maxi = max(maxi, (i - prevIdx) * prevHeight)
            stk.append((prevIdx, h))
        
        while stk:
            idx, h = stk.pop()
            maxi = max(maxi, (len(heights)- idx) * h)
            
        return maxi