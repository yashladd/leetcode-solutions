class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, prev2 = 1, 2
        for i in range(3, n+1):
            curr = prev + prev2
            prev = prev2
            prev2 = curr
        return prev2
            
            