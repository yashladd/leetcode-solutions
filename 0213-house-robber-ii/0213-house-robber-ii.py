class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        def f(nums):
            n = len(nums)
            if n <= 2:
                return max(nums)
            prev2, prev1 = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                tmp = prev1
                prev1 = max(prev1, nums[i] + prev2)
                prev2 = tmp
            
            return prev1

        return max(f(nums[:-1]), f(nums[1:]))