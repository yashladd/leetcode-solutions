class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def f(i, curr):
            if i == n:
                res.append(curr[:])
                return 
                
            f(i+1, curr)
            f(i+1, curr + [nums[i]])
        f(0, [])
        return res