class Solution:
    def longestStrChain(self, nums: List[str]) -> int:
        nums.sort(key = lambda x: len(x))
        def check(s1, s2):
            if len(s1) != len(s2) + 1: return False
            i, j = 0, 0
            nomatch = 0
            while j < len(s2):

                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    if nomatch == 1:
                        return False
                    nomatch += 1
                    i += 1
            return j == len(s2)

        n = len(nums)
        dp = [1] * n
        maxi = 1
        for i in range(n):
            for p in range(i):
                if check(nums[i], nums[p]) and dp[p] + 1 > dp[i]:
                    dp[i] = dp[p] + 1
                    maxi = max(maxi, dp[i])

        return maxi
            