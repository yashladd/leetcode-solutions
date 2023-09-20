class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        prev = nums[0]
        prev2 = max(nums[0], nums[1])
        for i in range(2, n):
            curr = max(prev2, nums[i] + prev)
            prev = prev2
            prev2 = curr
            # print(prev, prev2, curr)
        return prev2