class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last, cnt = {}, {}, {}
        for i, n in enumerate(nums):
            if n not in first:
                first[n] = i
            last[n] = i
            cnt[n] = cnt.get(n, 0) + 1
            
        res = len(nums)
        degree = max(cnt.values())
        for n in nums:
            if cnt[n] == degree:
                res = min(res, last[n] - first[n] + 1)
                
        return res