class Solution:
    def search(self, A: List[int], target: int) -> int:
        l, h = 0 , len(A) - 1
        while l <= h:
            m = (l + h) >> 1
            if A[m] == target: return m
            elif A[l] <= A[m]:
                if A[l] <= target and target <= A[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if A[m] <= target and target <= A[h]:
                    l = m + 1
                else:
                    h = m - 1
                
        return -1