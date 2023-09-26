class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for p in range(i):
                if nums[p] < nums[i]:
                    dp[i] = max(dp[i], dp[p] + 1)
        return max(dp)
            