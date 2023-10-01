class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        x=1
        for i in range(n):
            res[i] = x
            x *= nums[i]
            
        y = 1
        for i in reversed(range(n)):
            res[i] *= y
            y *= nums[i]
            
        return res
        
        