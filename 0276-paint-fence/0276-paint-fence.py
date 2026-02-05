class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        ways(1) = k
        ways(2) = k * k

        ways(i) = 
        1. Different color than i-1: k-1 * ways(i-1)
        2. Same color as i-1: 
            Only one choice 1 * ways(i-1) | Constraint i and i-1 are different colors
            Now ways i-1 different color than i-2 is actually k-1 * ways(i-2) from 1!

        Hence dp(i) = k-1 * dp(i-1) + k-1 * dp(i-2)
        """

        @cache
        def ways(idx):
            if idx == 1:
                return k
            
            if idx == 2:
                return k*k

            return (k-1) * (ways(idx-1) + ways(idx-2))

        return ways(n)

            

        