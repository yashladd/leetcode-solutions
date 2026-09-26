class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[]]


        @cache
        def f(i, b, t):
            if t == 0:
                return 0

            if i == len(prices):
                return 0

            if b:
                return max(
                    -prices[i] + f(i+1, 0, t),
                    f(i+1, 1, t)
                )
            
            return max(
                prices[i] + f(i, 1, t-1),
                f(i+1, 0, t)
            )

        return f(0, 1, 2)
        