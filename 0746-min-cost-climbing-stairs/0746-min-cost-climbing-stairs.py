class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def f(i):
            if i >= len(cost):
                return 0
            
            t = cost[i] + f(i + 1)
            nt = cost[i] + f(i + 2)
            
            return min(t, nt)
        
        return min(f(0), f(1))