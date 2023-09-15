class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, e, g = 0, 0, n-1
        
        while e <= g:
            if nums[e] == 2:
                nums[e], nums[g] = nums[g], nums[e]
                g -= 1
            elif nums[e] == 0:
                nums[e], nums[l] = nums[l], nums[e]
                l += 1
                e += 1
            else:
                e += 1