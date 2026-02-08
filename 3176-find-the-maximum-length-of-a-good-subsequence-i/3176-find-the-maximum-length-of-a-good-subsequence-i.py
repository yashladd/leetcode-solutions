class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][j] = max length of a good subsequence ending at index 'i' 
        # with exactly 'j' mismatches allowed.
        # Initialize with 1 because a single element is always a valid subsequence.
        dp = [[1] * (k + 1) for _ in range(n)]
        
        ans = 1
        
        for i in range(1,n):
            for j in range(k + 1):
                # Check all possible previous elements 'p'
                for p in range(i):
                    if nums[i] == nums[p]:
                        # If values match, we extend the sequence without using a 'change' budget
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                    elif j > 0:
                        # If values differ, we can extend only if we have budget (j > 0)
                        # We use one 'change' from the budget (transition from j-1)
                        dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1)
                
                # Track the global maximum length found
                ans = max(ans, dp[i][j])
                
        return ans