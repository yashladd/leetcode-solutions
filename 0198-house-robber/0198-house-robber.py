class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def f(n):
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            take = nums[n] + f(n-2)
            notTake = f(n-1)
            dp[n] = max(take, notTake)
            return max(take, notTake)
        return f(len(nums)-1)