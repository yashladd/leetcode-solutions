class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = float("inf")
        minPref = [INF] * k
        minPref[k-1] = 0

        ps = 0
        res = -INF
        for i, x in enumerate(nums):
            ps += x
            rem = i % k
            if i >= k:
                res = max(res, ps - minPref[rem])
            elif i == k-1:
                res = max(res, ps)

            minPref[rem] = min(minPref[rem], ps)
        return res


        