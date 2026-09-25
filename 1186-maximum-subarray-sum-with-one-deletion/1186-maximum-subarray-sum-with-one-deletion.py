class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        keep = best = arr[0]
        drop = -inf

        for x in arr[1:]:
            drop = max(keep, drop + x)
            keep = max(keep + x, x)
            best = max(best, keep, drop)

        return best