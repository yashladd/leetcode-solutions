from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Compute prefix sums.
        # prefix[i] will store the sum of elements from nums[0] to nums[i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        # Initialize answer to infinity to find the minimum length later
        ans = float('inf')
        
        # Step 2: Monotonic queue to store indices of the prefix sum array.
        # It will keep the prefix sums in increasing order.
        dq = deque()
        
        for i in range(n + 1):
            # Check if we have a valid subarray:
            # If the current prefix sum minus the smallest prefix sum we've seen 
            # (at the front of the queue) is >= k, we found a valid subarray!
            while dq and prefix[i] - prefix[dq[0]] >= k:
                # Update the shortest length and pop the front.
                # We pop it because any future index would create a longer subarray,
                # and we only care about the shortest one.
                ans = min(ans, i - dq.popleft())
                
            # Maintain the monotonic property:
            # If the current prefix sum is smaller than or equal to the sum at the back 
            # of our queue, the back element is useless. The current one is both 
            # smaller AND closer to future elements, making it a better starting point.
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
                
            # Add the current index to the queue
            dq.append(i)
            
        return ans if ans != float('inf') else -1