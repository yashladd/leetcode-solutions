class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = nums[0]
        
        for n in nums[1:]:
            curr = max(n, n + curr)
            maxi = max(maxi, curr)
            
        return maxi
        