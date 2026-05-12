class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # Create a DP table padded with infinity
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Set dummy health requirements right outside the destination
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        
        # Work backwards from the bottom-right to the top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # The minimum health we need for the next step
                min_health_next = min(dp[i+1][j], dp[i][j+1])
                
                # Health needed before entering current room
                dp[i][j] = max(1, min_health_next - dungeon[i][j])
                
        return dp[0][0]