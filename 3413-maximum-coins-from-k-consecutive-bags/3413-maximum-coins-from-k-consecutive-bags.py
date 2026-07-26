class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        return max(
            self._best_left_aligned(coins, k),
            self._best_left_aligned([[-r, -l, c] for l, r, c in coins], k)
        )

    def _best_left_aligned(self, segs, k):
        segs = sorted(segs)
        N = len(segs)
        pref = [0] * (N+1)
        starts = [l for l, r, c in segs]

        for i, (l, r, c) in enumerate(segs):
            pref[i+1] = pref[i] + (r-l+1) * c

        best = 0

        for i, (l, r, c) in enumerate(segs):
            start = l
            end = l + k - 1

            j = bisect_right(starts, end) - 1

            curr_total = pref[j] - pref[i]
            l_j, r_j, c_j = segs[j]
            clipped_segment = min(r_j, end) - l_j + 1
            clipped_amount = clipped_segment * c_j

            best = max(best, curr_total + clipped_amount)

        return best