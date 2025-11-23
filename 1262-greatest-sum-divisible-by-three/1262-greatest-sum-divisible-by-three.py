class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        n = len(nums)
        INF = float("inf")

        prev = [0, -INF, -INF]
        for i in range(1, n+1):
            curr = [-INF, -INF, -INF]
            for m in range(3):
                best = -float('inf')
                best = max(best, prev[(nums[i-1] + m)%3] + nums[i-1])
                best = max(best, prev[m])
                curr[m] = best

            prev = curr[:]

        return prev[0]
