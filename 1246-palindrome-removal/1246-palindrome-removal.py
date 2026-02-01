from functools import cache
from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        @cache
        def dp(i, j):
            # Base Case: Empty range requires 0 moves
            if i > j:
                return 0
            
            # Base Case: Single element requires 1 move
            if i == j:
                return 1
            
            # Transition 1: Remove the first element alone
            # Cost is 1 (for arr[i]) + cost for the rest
            res = 1 + dp(i + 1, j) #
            
            # Transition 2: Try to merge arr[i] with a matching arr[k]
            # Iterate through all k > i where arr[i] == arr[k]
            for k in range(i + 1, j + 1):
                if arr[i] == arr[k]:
                    # We match arr[i] and arr[k].
                    # We solve the inner part (i+1 to k-1) and the outer part (k+1 to j).
                    # 'max(1, ...)' ensures that if the inner part is empty (e.g. [1,1]), 
                    # the cost is 1 (remove the pair), not 0.
                    merged_cost = max(1, dp(i + 1, k - 1)) + dp(k + 1, j) #
                    
                    res = min(merged_cost, res)
            
            return res

        return dp(0, len(arr) - 1)