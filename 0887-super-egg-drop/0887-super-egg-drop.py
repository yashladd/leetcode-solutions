from functools import lru_cache

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        @lru_cache(None)
        def f(m, egs):
            # Base cases
            if egs == 1: return m
            if m <= 1: return m
            
            mini = float('inf')
            
            # Binary Search for the optimal floor 'i'
            low, high = 1, m
            while low <= high:
                mid = (low + high) // 2
                
                # If egg breaks: we check floors below (left side)
                # This function is increasing with mid
                broken = f(mid - 1, egs - 1)
                
                # If egg survives: we check floors above (right side)
                # This function is decreasing with mid
                survived = f(m - mid, egs)
                
                # We want the minimum of the worst-case scenario
                res = 1 + max(broken, survived)
                mini = min(mini, res)
                
                if broken < survived:
                    # The 'survived' side is more expensive, 
                    # try a higher floor to increase 'broken' and decrease 'survived'
                    low = mid + 1
                elif broken > survived:
                    # The 'broken' side is more expensive, 
                    # try a lower floor to decrease 'broken'
                    high = mid - 1
                else:
                    # Perfectly balanced
                    break
                    
            return mini
        
        return f(n, k)