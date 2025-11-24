class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        for i in range(1, len(nums)):
            nums[i] = nums[i-1] * 2 + nums[i]

        return list(map(lambda x: x%5 == 0, nums))