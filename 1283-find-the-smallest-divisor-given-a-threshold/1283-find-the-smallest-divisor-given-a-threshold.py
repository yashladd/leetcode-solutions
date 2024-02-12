class Solution:
    def smallestDivisor(self, a: List[int], threshold: int) -> int:
        l, r = 1, max(a)
        def canMake(mid):
            res = 0
            for n in a:
                res += ceil(n/mid)
            return res <= threshold
        ans = r
        while l <= r:
            mid = (l + r) >> 1
            if canMake(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans