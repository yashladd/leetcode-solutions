class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        c = 0
        mini = 0
        for i in range(len(nums)):
            c += nums[i]
            
            if c < 1:
                # x + start =  1
                mini = max(mini, 1 - c)
                
        return mini if mini != 0 else 1