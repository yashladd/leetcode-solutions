class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        h = [i for i in range(n)]
        maxi = 0
        for i in range(1, n):
            for p in range(i):
                if not nums[i] % nums[p]:
                    if dp[p] + 1 > dp[i]:
                            dp[i] = dp[p] + 1
                            h[i] = p
                            if dp[i] > dp[maxi]:
                                maxi = i

        res = []
        i = maxi
        while h[i] != i:
            res.append(nums[i])
            i = h[i]
        res.append(nums[i])
        return res
            

        