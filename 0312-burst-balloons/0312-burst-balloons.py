class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @cache
        def f(i, j):
            if i > j: return 0
            c = float("-inf")
            for k in range(i, j+1):
                cost = nums[k] * nums[i-1] * nums[j+1] + f(i, k-1) + f(k+1, j)
                c=max(c, cost)
            return c

        return f(1, n)

        