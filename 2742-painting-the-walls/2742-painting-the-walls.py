class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        n = len(time)
        dp = [ [0] * (n + 1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[n][i] = inf

        prev=[inf] * (n+1)

        prev[0] = 0
        for i in range(n-1, -1, -1):
            curr = [inf] * (n+1)
            curr[0] = 0
            for remain in range(1, n+1):
                take = cost[i] + prev[max(0, remain - 1 - time[i])]
                notTake = prev[remain]
                curr[remain] = min(take, notTake)
            prev= curr
        return prev[n]

        @cache
        def f(i, remain):
            if remain <= 0:
                return 0
            if i == n:
                return inf
            take = cost[i] + f(i+1, remain - 1 - time[i])
            notTake = f(i+1, remain)
            return min(take, notTake)


        return f(0, len(time))
        