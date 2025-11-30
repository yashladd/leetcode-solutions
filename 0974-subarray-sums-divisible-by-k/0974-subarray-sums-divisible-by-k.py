class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        pref = 0
        h = defaultdict(int)
        h[0] = 1
        for i, x in enumerate(nums):
            pref = (pref + x) % k
            if pref in h:
                res += h[pref]
            h[pref] += 1

        return res
            

        