class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n + 1)for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for p in range(i-1, -2, -1):
                take, notTake = 0, 0
                if p == -1 or nums[i] > nums[p]:
                    take =  1 + dp[i + 1][i+1]
                
                notTake = dp[i+1][p+1]
                dp[i][p+1] = max(take, notTake)
        return dp[0][0]
        def lis(i, p):
            if i == n:
                return 0
            if dp[i][p+1]!=-1:
                return dp[i][p+1]
            take, notTake = 0, 0
            if p == -1 or nums[i] > nums[p]:
                take =  1 + lis(i + 1, i)
                
            notTake = lis(i+1, p)
            dp[i][p+1] = max(take, notTake)
            return max(take, notTake)
        
        return lis(0, -1)
            