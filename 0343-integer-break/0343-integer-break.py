class Solution:
    def integerBreak(self, n: int) -> int:
        """
            10 -> 1, 2, 3, ... 9
               1 * f(9)
               2 * f(8)
               3 * f(7)

               f(7) -> 1 * f(6), 2 * f(5), 3 * f(4)     
        """

        dp = [ 0 ] * (n+1)
        dp[1] = 1

        for i in range(1, n+1):
            maxi = 0 if i == n else i
            for x in range(1, i):
                maxi = max(maxi, dp[x] * dp[i-x])
            dp[i] = maxi
        return dp[n]


        def f(i):
            if i == 1:
                return 1
            
            maxi = 0 if i == n else i
            for x in range(1, i):
                maxi = max(maxi, f(x) * f(i-x))
            return maxi

        return f(n)

        