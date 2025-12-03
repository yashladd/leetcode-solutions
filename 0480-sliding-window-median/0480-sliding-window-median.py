import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # small: max-heap (stores negatives)
        # large: min-heap
        small, large = [], []
        # invalid: tracks counts of numbers that have left the window but are still in heaps
        invalid = defaultdict(int)
        
        # Explicitly track the size of valid elements in each heap
        small_size = 0
        large_size = 0
        
        def prune(heap, is_small):
            # Remove invalid elements from the top of the heap
            while heap:
                val = -heap[0] if is_small else heap[0]
                if invalid[val] > 0:
                    invalid[val] -= 1
                    heapq.heappop(heap)
                else:
                    break
        
        result = []
        
        for i, num in enumerate(nums):
            # --- 1. Add New Element ---
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            
            # --- 2. Remove Old Element (Lazy) ---
            if i >= k:
                out_num = nums[i - k]
                invalid[out_num] += 1
                
                # Determine which heap the removed element belonged to logically
                # Note: We rely on the current top of 'small' to decide.
                # Even if 'small' has garbage at the top, the logic holds because 
                # the element was inserted based on this same boundary.
                if out_num <= -small[0]:
                    small_size -= 1
                else:
                    large_size -= 1
                
                # Prune tops immediately to ensure heap[0] is valid for rebalancing
                prune(small, True)
                prune(large, False)

            # --- 3. Rebalance Heaps ---
            # Invariant: small_size can be equal to large_size OR large_size + 1
            
            # If small is too big (more than 1 element larger than large)
            while small_size > large_size + 1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)
                small_size -= 1
                large_size += 1
                prune(small, True) # Prune after pop exposes new top

            # If large is bigger than small (small must be >= large)
            while large_size > small_size:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                large_size -= 1
                small_size += 1
                prune(large, False) # Prune after pop exposes new top

            # --- 4. Get Median ---
            if i >= k - 1:
                if k % 2 == 1:
                    result.append(-small[0])
                else:
                    result.append((-small[0] + large[0]) / 2)
                    
        return result