class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l = 0
        h = n - 1
        while l <= h:
            m = (l + h) >> 1
            missing = arr[m] - m - 1
            if missing < k:
                l = m + 1
            else: 
                h = m - 1
                
        return 1 + h + k