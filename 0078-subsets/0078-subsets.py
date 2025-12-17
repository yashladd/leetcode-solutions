class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(i, s):
            if i == len(nums):
                res.append(s[:])
                return 

            f(i+1, s)
            f(i + 1, s + [nums[i]])
        f(0, [])
        return res