class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pref = [0] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i-1]
        for i in range(len(nums)-1, 1,-1):
            if pref[i] > nums[i]:
                return pref[i] + nums[i]
        return -1


        