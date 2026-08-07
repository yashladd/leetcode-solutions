from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp stores {current_sum: number_of_ways}
        dp = defaultdict(int)
        dp[0] = 1  # Base case: 1 way to get sum 0 using 0 elements
        
        for num in nums:
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum + num] += count
                next_dp[curr_sum - num] += count
            dp = next_dp  # Move to the next "row"
            
        return dp[target]