class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def f(n, k):
            if n == 1:
                return 0

            return (f(n-1, k) + k) % n

        return f(n, k)  + 1