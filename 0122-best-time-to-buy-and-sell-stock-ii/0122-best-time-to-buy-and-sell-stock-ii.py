class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prof = 0

        mini = prices[0]

        for i in range(1, len(prices)):
            curr = prices[i]

            if curr > mini:
                prof += (curr - mini)
                mini = curr
            else:
                mini = curr

        return prof