class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        @cache
        def f(i, t):
            if i == n-1:
                return 1 if not t % coins[n-1] else 0
            
            if t == 0:
                return 1
            
            if t < 0:
                return 0
            
            return f(i, t - coins[i]) + f(i+1, t)
        
        
        return f(0, amount)
        