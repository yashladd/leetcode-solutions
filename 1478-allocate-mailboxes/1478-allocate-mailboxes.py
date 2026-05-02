class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()

        # 1. Initialize a 2D array with zeros
        cost = [[0] * n for _ in range(n)]

        # 2. Fill the cost array
        for i in range(n):
            for j in range(i, n):
                median_idx = (i + j) // 2
                for x in range(i, j + 1):
                    cost[i][j] += abs(houses[x] - houses[median_idx])

        # 3. Now your DP transition is lightning fast!
        @cache
        def f(i, k):
            if k == 0: return 0 if i == n else float('inf')
            if i == n: return 0
            
            mini = float('inf')
            for j in range(i, n):
                # Instead of calling a function that loops, 
                # just grab the precomputed value
                curr_dist = cost[i][j] 
                mini = min(mini, curr_dist + f(j + 1, k - 1))
            return mini

        return f(0, k)