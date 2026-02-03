class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        """
        up_cos * (server) <= money

        up_cos * (n - x) <= money + x * sell_cost

        n * up_cos - money / ((sell_cos + up_cos))  <=  x 

        4 * 3 - 8 / (4 + 3)

        """
        res = []
        for c, u, s, m in zip(count, upgrade, sell, money):
            to_sell = ceil((c*u - m)/(s + u))
            res.append(c - to_sell if to_sell > 0 else c)
        return res