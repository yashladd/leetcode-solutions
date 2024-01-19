class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def rec(i, a):
            if i == n:
                res.append(a[:])
                return 
            
            # res.append(a[:])
            for j in range(i, n):
                a[i], a[j] = a[j], a[i]
                rec(i + 1, a)
                a[i], a[j] = a[j], a[i]
                
        rec(0, nums)
        return res
        
        