class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def f(x):
            if x == 1 or x == 2:
                return x
            
            if x == 0:
                return 1
            
            res = 0
            for i in range(x):
                lef = f(i)
                rig = f(x-i-1)
                res += (lef * rig)
            return res
        
        return f(n)
                
                
                
        