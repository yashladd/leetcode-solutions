class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        costs = [-x for x in cost]
        heapify(costs)

        res = 0

        while len(costs) > 2:
            best = -heappop(costs)
            sec_best = -heappop(costs)
            heappop(costs)
            res += best
            res += sec_best

        return res - sum(costs)
        