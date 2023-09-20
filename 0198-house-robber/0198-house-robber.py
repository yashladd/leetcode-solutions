class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
        return dp[n-1]
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