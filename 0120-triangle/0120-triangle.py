class Solution:
    def minimumTotal(self, a: List[List[int]]) -> int:
        n = len(a)
        @cache
        def f(i, j):
            if i == n-1:
                return a[n-1][j]
            
            return min(a[i][j] + f(i+1, j), a[i][j] + f(i+1, j+1))
        
        return f(0, 0)
            
            
        