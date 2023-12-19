class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        n=len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            if nums[l] <= nums[m]:
                mini = min(mini, nums[l])
                l = m + 1
            else:
                mini = min(mini, nums[m])
                r = m-1
        return mini
        