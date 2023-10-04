class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pref = [height[0]]
        currMax = height[0]
        for i in range(1, n):
            currMax = max(currMax, height[i])
            pref.append(currMax)
        
        suff = [height[n-1]]
        currMax = suff[-1]
        for i in range(n-2, -1, -1):
            currMax = max(currMax, height[i])
            suff.append(currMax)
        
        water = 0
        for l, r, h in zip(pref, suff[::-1], height):
            water += min(l, r) - h
            
        return water
            