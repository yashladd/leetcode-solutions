class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        last = len(nums)-1
        i = 0
        while i <= pos and pos < last:
            pos = max(pos, i + nums[i])
            i += 1
            
        return pos >= last