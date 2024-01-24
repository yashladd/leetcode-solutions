class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def fn(n):
            if n <= 1: return n
            return 1 + min(n%2 + fn(n//2), n%3 + fn(n//3))
        
        return fn(n)
            