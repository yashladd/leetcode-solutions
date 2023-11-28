class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def f(i, b):
            if i >=  n:
                return 0
            
            if i == n-1:
                if not b:
                    return prices[n-1]
                else:
                    return 0
                
            if b:
                t = -prices[i] + f(i+1, 0)
                nt = f(i+1, 1)
            else:
                t = prices[i] + f(i+2, 1)
                nt = f(i+1, 0)
                
            return max(0, t, nt)
        
        return f(0, 1)
                
                
            
        