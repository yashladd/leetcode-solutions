class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        n = len(coins)

        dp = [[0]*(amount + 1) for _ in range(n)]
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = float("inf")

        for i in range(1, n):
            for t in range(amount + 1):
                take = float("inf")
                if t >= coins[i]:
                    take = 1 + dp[i][t - coins[i]]
                ntake = dp[i-1][t]
                dp[i][t] = min(take, ntake)

        return dp[n-1][amount] if dp[n-1][amount] != float("inf") else -1
        
        def f(idx, t):
            if idx == 0:
                if t % coins[idx] == 0:
                    return t // coins[idx]
                return float("inf")

            if dp[idx][t] != -1:
                return dp[idx][t]

            take = float("inf")
            if t >= coins[idx]:
                take = 1 + f(idx, t - coins[idx])
            nottake = 0 + f(idx-1, t)
            dp[idx][t] = min(take, nottake)
            return dp[idx][t]

        res = f(n-1, amount) 
        return res if res != float("inf") else -1

        # for i in range(1, n):
        #     for j in range(amount+1):
        #         o, t, r = float("inf"),float("inf"),   float("inf")
        #         z = j - coins[i]
        #         if z >= 0:
        #             o = 1 + dp[i][z]
        #             t = 1 + dp[i-1][z]
        #         r = dp[i-1][j]
        #         dp[i][j] = min(o,t, r)

        # return dp[n-1][amount]


        