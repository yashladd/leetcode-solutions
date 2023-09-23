class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                
            tmpCurMax = n * curMax
            curMax = max(tmpCurMax, n * curMin, n)
            curMin = min(tmpCurMax, n * curMin, n)
            
            res = max(res, curMax)
            
        return res
            
        