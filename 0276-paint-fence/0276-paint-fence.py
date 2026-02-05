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
        if n == 0:
            return 0

        if n == 1:
            return k
            
        if n == 2:
            return k*k

        prev1, prev2 = k*k, k
        for i in range(3, n+1):
            curr = (k-1) * (prev1 + prev2)
            prev1, prev2 = curr, prev1

        return prev1

        @cache
        def ways(idx):
            if idx == 1:
                return k
            
            if idx == 2:
                return k*k

            return (k-1) * (ways(idx-1) + ways(idx-2))

        return ways(n)

            

        