class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        res = []
        def f(i, curr):
            res.append(curr[:])
            for j in range(i, N):
                f(j+1, curr + [nums[j]])

        f(0, [])

        return res

