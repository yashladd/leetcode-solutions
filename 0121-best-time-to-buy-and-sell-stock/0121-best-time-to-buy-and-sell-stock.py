class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = float("inf")
        for p in prices:
            res = max(res, p - mini)
            mini = min(mini, p)
        return res