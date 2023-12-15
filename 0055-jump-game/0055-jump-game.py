class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [-1] * (n+1)
        @cache
        def f(i):
            if i >= n:
                return True
            
            if i + nums[i] >= n-1:
                return True
            
            for j in range(i+1, i + nums[i]+1):
                if f(j):
                    return True
                
            return False
        
        return f(0)