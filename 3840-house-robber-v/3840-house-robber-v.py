class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        N = len(nums)
        @cache
        def rob(i):
            if i >= N:
                return 0

            nottake = rob(i+1)
            take = nums[i]
            if i + 1 < N and colors[i+1] != colors[i]:
                take += rob(i+1)
            elif i + 2 < N:
                take += rob(i+2)

            return max(take, nottake)

        return rob(0)

