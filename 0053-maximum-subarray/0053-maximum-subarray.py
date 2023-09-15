class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end_here = 0
        max_so_far = float("-inf")
        for num in nums:
            max_end_here = max(max_end_here + num, num)
            max_so_far = max(max_so_far, max_end_here)
            
        return max_so_far