class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            sortedIdx = num - 1
            if 1 <= num <= n and nums[i] != nums[sortedIdx]:
                nums[i], nums[sortedIdx] = nums[sortedIdx], nums[i]
                # i += 
            else:
                i += 1

        for i in range(n):
            if i != nums[i] - 1:
                return i + 1

        return n + 1
        