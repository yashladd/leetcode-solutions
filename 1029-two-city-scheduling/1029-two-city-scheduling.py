class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        [[10,20],[30,200],[400,50],[30,20]]
        aCosts = [10, 30, 30, 400]
        bCosts = [20, 20, 50, 200]

        """
        n = len(costs) // 2
        N=len(costs)
        # print(f"N {n}")
        @cache
        def f(i, a, b):
            # print(f"f {i} {a} {b}")
            if i == N:
                if a == n and b == n:
                    return 0
                return float("inf")

            takeA = float("inf")
            if a + 1 <= n:
                takeA = costs[i][0] + f(i+1, a + 1, b)

            takeB = float("inf")
            if b + 1 <= n:
                takeB = costs[i][1] + f(i+1, a, b + 1)

            return min(takeA, takeB)
        val = f(0, 0, 0)
        # print(val)
        return val
            

        