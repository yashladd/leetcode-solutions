class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:

        

        def max_amount_left_aligned(coins):
            coins = sorted(coins)
            N = len(coins)

            pref_amount = [0] * (N+1)

            for i, (l, r, c) in enumerate(coins):
                pref_amount[i+1] = pref_amount[i] + (r - l + 1) * c

            interval_starts = [l for l, _, _  in coins]
            best = 0
            for i, (l, r, c) in enumerate(coins):
                start = l
                end = l + k - 1

                j = bisect_right(interval_starts, end) - 1

                l_j, r_j, c_j = coins[j]

                amount = pref_amount[j] - pref_amount[i]

                partial_amount = (min(end, r_j) - l_j  + 1) * c_j

                amount += partial_amount

                best = max(best, amount)

            return best


        return max(
            max_amount_left_aligned(coins),
            max_amount_left_aligned([(-r, -l, c) for l, r, c in coins])
        )

