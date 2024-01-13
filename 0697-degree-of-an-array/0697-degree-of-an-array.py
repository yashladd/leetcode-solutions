class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, cnt = {}, {}
        res = len(nums)
        degree = -float("inf")
        for i, n in enumerate(nums):
            fIdx = first.setdefault(n, i)
            cnt[n] = cnt.get(n, 0) + 1
            if cnt[n] > degree:
                degree = cnt[n]
                res = i - fIdx + 1
            elif cnt[n] == degree:
                res = min(res, i - fIdx + 1)
                
        return res