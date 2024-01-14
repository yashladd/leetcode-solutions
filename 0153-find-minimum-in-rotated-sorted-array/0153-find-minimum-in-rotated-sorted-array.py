class Solution:
    def findMin(self, A: List[int]) -> int:
        l, h = 0 , len(A) - 1
        mini = float("inf")
        while l <= h:
            m = (l + h) >> 1
            if A[l] <= A[m]:
                mini = min(mini, A[l])
                l = m + 1
            else:
                mini = min(mini, A[m])
                h = m - 1
                
        return mini
                
        