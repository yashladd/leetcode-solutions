class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        farthestIdx = 0

        for i, j in enumerate(nums):
            if i > farthestIdx: return False 
            if farthestIdx >= n:
                return True
            farthestIdx = max(farthestIdx, j + i)

        return farthestIdx >= n-1