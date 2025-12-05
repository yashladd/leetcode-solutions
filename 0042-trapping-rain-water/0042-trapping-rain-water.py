class Solution:
    def trap(self, h: List[int]) -> int:
        """
        
        0 1 2 0 3 4 5

        """

        res = 0
        l, r = 0, len(h)-1

        

        lMax, rMax = 0, 0

        while l <= r:
            if h[l] <= h[r]:
                if h[l] < lMax and lMax > 0:
                    res += lMax - h[l]
                lMax = max(h[l], lMax)
                l += 1
            else:
                if h[r] < rMax and rMax > 0:
                    res += rMax - h[r]
                rMax = max(h[r], rMax)
                r -= 1

        return res