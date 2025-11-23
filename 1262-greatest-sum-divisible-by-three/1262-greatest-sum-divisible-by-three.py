class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [[-float("inf") for _ in range(3)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for m in range(3):
                best = -float('inf')
                best = max(best, dp[i-1][(nums[i-1] + m)%3] + nums[i-1])
                best = max(best, dp[i-1][m])
                dp[i][m] = best

        return dp[n][0]


        @cache
        def f(i, m):
            if i < 0:
                return 0 if not m else -float("inf")

            best = f(i-1, (nums[i] + m)%3) + nums[i]

            best = max(best, f(i-1, m))

            return best

        return f(n-1, 0)