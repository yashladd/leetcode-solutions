class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def f(i):
            if i == n-1:
                return 0
            
            if i < n-1 and i + nums[i] >= n-1:
                return 1
            
            mini = 1 + f(i + 1)
            for j in range(i+2, i + nums[i] + 1):
                mini = min(1 + f(j), mini)

            return mini
        
        return f(0)
        