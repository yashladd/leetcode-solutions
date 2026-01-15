class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            correctIdx = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correctIdx]:
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i += 1


        # for i in range(n):
        #     # num = nums[i]
            
        #     while 1 <= nums[i] <= n and nums[i] - 1 != i:
        #         idxToSwap = nums[i] - 1
        #         nums[i], nums[idxToSwap] = nums[idxToSwap], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
        