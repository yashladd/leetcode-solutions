class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums))
        pi, ni = 0, 1
        for n in nums:
            if n < 0:
                res[ni] = n
                ni += 2
            else:
                res[pi] = n
                pi += 2
        return res
        