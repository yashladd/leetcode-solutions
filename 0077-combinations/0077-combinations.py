class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        a = [i for i in range(1, n+1)]
        
        def f(i, ds):
            if len(ds) == k:
                res.append(ds[:])
                return 
            for j in range(i, n):
                f(j+1, ds + [a[j]])
                
                
        f(0, [])
        return res
                
        