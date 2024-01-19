class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        
        
        def isPal(l, r):
            t = s[l:r+1]
            return t == t[::-1]
        
        def f(i, ds):
            if i == n:
                res.append(ds[:])
                return 
            
            for j in range(i, n):
                if isPal(i, j):
                    f(j+1, ds + [s[i:j+1]])
                    
        f(0, [])
        return res
                