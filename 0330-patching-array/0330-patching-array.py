class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        maxReachable = 0
        i = 0
        patches = 0


        while maxReachable < n:
            if i < n and nums[i] <= maxReachable + 1:
                maxReachable += nums[i]
                i += 1
            else:
                maxReachable += (maxReachable+1)
                patches += 1

        return patches