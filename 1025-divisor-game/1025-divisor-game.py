class Solution:
    def divisorGame(self, n: int) -> bool:

        @cache
        def f(n):
            if n == 1:
                return False
            
            for x in range(n-1, 0, -1):
                if not n % x:
                    if not f(n-x):
                        return True

            return False

        

        return f(n)
        
        