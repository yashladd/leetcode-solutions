class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo = min(nums)
        hi = max(nums)
        res = hi

        def can_rob(x):

            i = 0
            robbed = 0
            while i < len(nums):
                if nums[i] <= x:
                    robbed += 1
                    i += 2
                else:
                    i += 1

            return robbed >= k


        while lo <= hi:
            mi = (lo + hi) >> 1

            if can_rob(mi):
                res = mi
                hi = mi - 1
            else:
                lo = mi + 1

        return res
