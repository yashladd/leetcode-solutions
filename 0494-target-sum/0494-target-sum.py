class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        @cache
        def f(idx, t):
            if idx == 0:
                ways = 0
                if t - nums[idx] == 0:
                    ways += 1
                if t + nums[idx] == 0:
                    ways += 1
                return ways
            
            pos =  f(idx-1, t - nums[idx])
            neg =  f(idx-1, t + nums[idx])
            
            return pos + neg
        
        return f(n-1, target)
        