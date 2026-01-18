class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        r = n-1

        l = 0
        res = 0
        while r >= 0 and nums[r] == val:
            res += 1
            r -= 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                res += 1
            else:
                l += 1

        return n  - res
        