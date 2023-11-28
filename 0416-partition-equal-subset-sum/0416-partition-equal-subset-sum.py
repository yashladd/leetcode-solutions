class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 2:
            return False

        k = s//2
        dp = [[-1] * (k + 1) for _ in range(len(arr))]
        def f(i, t):
            if t == 0:
                return True
            if i == 0:
                return arr[i] == t

            if dp[i][t] != -1:
                return dp[i][t]

            take = f(i-1, t)
            notTake = False
            if arr[i] <= t:
                notTake =f(i-1, t - arr[i])
            
            dp[i][t] = take or notTake
            return take or notTake

        return f(len(arr)-1, k)
            
            
            
        
        