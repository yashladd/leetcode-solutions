class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        
        if len(a) == 1:
            return 0
        if a[0] > a[1]: return 0
        if a[len(a)-1] > a[len(a) - 2]: return len(a)-1
        l, r = 1, len(a) - 2
        while l <= r:
            m = (l + r) >> 1
            if  a[m] > a[m-1] and a[m+1] < a[m]:
                return m

            if a[m] > a[m-1]:
                l = m + 1
            else:
                r = m - 1 
        