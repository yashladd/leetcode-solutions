class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        [1,2,3,4,3]
        1 2 3 4 3 1 2 3 4
        
        
        """
        
        stk = nums[:-1][::-1]
        
        n = len(nums)
        
        
        res = [-1] * n
        
        
        for i in range(n-1, -1, -1):
            curr = nums[i]
            
            while stk and stk[-1] <= curr:
                stk.pop()
                
            if stk:
                res[i] = stk[-1]
            
            stk.append(curr)
            
        return res
        
        
        