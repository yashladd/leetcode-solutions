class Solution:
    def canJump(self, nums):
        N = len(nums)
        maxIdx = 0
        for i in range(N-1):
            if maxIdx < i:
                return False
            maxIdx = max(maxIdx, i + nums[i])
            if maxIdx >= N-1:
                return True
        return maxIdx >= N-1