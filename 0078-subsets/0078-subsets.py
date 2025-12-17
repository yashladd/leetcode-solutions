class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def rec(i, res, out):
            out.append(res)
            for j in range(i, len(nums)):
                rec(j + 1, res + [nums[j]], out)              
        rec(0, [], out)
        return out
            