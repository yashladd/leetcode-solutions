class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        keep = nums[0]
        best = nums[0]
        for x in nums[1:]:
            keep = max(keep + x, x)
            best = max(best, keep)


        return best