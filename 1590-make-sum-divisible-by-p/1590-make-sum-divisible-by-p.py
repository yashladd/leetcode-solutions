class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalMod = 0
        for x in nums:
            totalMod = (totalMod + x) % p

        if totalMod == 0:
            return 0
        ans = len(nums)
        h = {0: -1}
        prefMod = 0
        for i, x in enumerate(nums):
            prefMod = (prefMod + x) % p
            if ((prefMod - totalMod + p) % p) in h:
                ans = min(ans , i  - h[(prefMod - totalMod + p) % p])
            h[prefMod] = i

        return -1 if ans == len(nums) else ans

        