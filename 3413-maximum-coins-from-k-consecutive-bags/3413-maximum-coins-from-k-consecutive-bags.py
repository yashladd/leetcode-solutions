class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def best_left_aligned(segs):
            segs.sort()
            starts = [s[0] for s in segs]
            pre = [0] * (len(segs) + 1)              # pre[i] = coins in segs[0..i-1]
            for i, (l, r, c) in enumerate(segs):
                pre[i+1] = pre[i] + (r - l + 1) * c

            best = 0
            for i, (l, _, _) in enumerate(segs):
                end = l + k - 1                       # window is [l, end]
                j = bisect_right(starts, end) - 1     # last segment that starts inside
                total = pre[j] - pre[i]               # segments i..j-1: fully inside
                lj, rj, cj = segs[j]                  # segment j: maybe clipped
                total += (min(rj, end) - lj + 1) * cj
                best = max(best, total)
            return best

        return max(
            best_left_aligned(coins),
            best_left_aligned([[-r, -l, c] for l, r, c in coins]),
        )