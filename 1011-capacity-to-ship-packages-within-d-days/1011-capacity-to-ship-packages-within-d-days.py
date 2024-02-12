class Solution:
    def shipWithinDays(self, a: List[int], threshold: int) -> int:
        l, r = max(a), sum(a)
        def canMake(mid):
            days, wt = 1, 0
            for n in a:
                if wt + n <= mid:
                    wt += n
                else:
                    days += 1
                    wt = n
            return days <= threshold
        ans = r
        while l <= r:
            mid = (l + r) >> 1
            if canMake(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans