class Solution:
    def trap(self, a: List[int]) -> int:
        n = len(a)
        l, r = 0, n-1
        lmax, rmax = 0, 0
        w = 0
        while l < r:
            if a[l] <= a[r]:
                if a[l] >= lmax:
                    lmax = a[l]
                else:
                    w += (lmax - a[l])
                l += 1
            else:
                if a[r] >= rmax:
                    rmax = a[r]
                else:
                    w += (rmax - a[r])
                    
                r-= 1
                
        return w
        
            