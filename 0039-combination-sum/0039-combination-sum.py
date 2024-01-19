class Solution:
    def combinationSum(self, a: List[int], target: int) -> List[List[int]]:
        n = len(a)
        res = []
        def rec(i, t, ds):
            if t == 0:
                res.append(ds[:])
                return 
                
            if i == n or t < 0:
                return 
            
            rec(i, t - a[i], ds + [a[i]])
            rec(i + 1, t, ds)
            
            
        rec(0, target,[])
        return res
            
        
        
        
        