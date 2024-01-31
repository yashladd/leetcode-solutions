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
                # print(i, range(0, i-1), range(i+1, x), len(range(0, i-1)), len(range(i+1, x)))
                lef = f(len(range(0, i)))
                rig = f(len(range(i+1, x)))
                # print(res, lef, rig)
                res += (lef * rig)
            return res
        
        return f(n)
                
                
                
        