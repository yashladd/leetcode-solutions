class Solution:
    def maximumProfit(self, present: list[int], future: list[int], budget: int) -> int:
        # dp[i] represents the max profit achievable with a budget of i
        dp = [0] * (budget + 1)
        
        for p, f in zip(present, future):
            profit = f - p
            # Only consider stocks that yield a positive profit
            if profit > 0:
                # Traverse backward to ensure each stock is picked at most once
                for b in range(budget, p - 1, -1):
                    dp[b] = max(dp[b], dp[b - p] + profit)
                    
        return dp[budget]