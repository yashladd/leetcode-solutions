class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maxi = 0, nums[0]
        for n in nums:
            curr = max(curr+n, n)
            maxi = max(maxi, curr)
        return maxi