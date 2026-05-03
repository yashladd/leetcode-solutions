class Solution:
    def canCross(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if n == 1:
            return True
        @cache
        def f(i, p):
            if i == n-1:
                return True
            
            
            for j in range(i+1, n):
                jump = nums[j] - nums[i]
                
                if p-1 <= jump <= p+1:
                    if f(j, jump):
                        return True
    
            
            return False
        
        if n >= 2:
            if nums[1] - nums[0] > 1:
                return False
            
            return f(1, 1)
        
        
                    
        