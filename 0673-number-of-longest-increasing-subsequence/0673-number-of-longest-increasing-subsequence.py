class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n

        maxi = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    cnt[i] = cnt[j]
                elif nums[i] > nums[j] and dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]

            if dp[i] > maxi:
                maxi = dp[i]

        res = 0
        for i in range(n):
            if dp[i] == maxi:
                res += cnt[i]

        return res

        