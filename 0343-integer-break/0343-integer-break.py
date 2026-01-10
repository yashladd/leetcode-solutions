class Solution:
    def integerBreak(self, n: int) -> int:
        """
            10 -> 1, 2, 3, ... 9
               1 * f(9)
               2 * f(8)
               3 * f(7)

               f(7) -> 1 * f(6), 2 * f(5), 3 * f(4)     
        """
        if n <= 3:
            return n-1
        @cache
        def f(x):
            if x <= 3:
                return x
            maxi = 0
            for i in range(2, x):
                maxi = max(maxi, i * f(x-i))

            return maxi

        return f(n)
