import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        
        # 1. Split into three piles
        left =  [x for x in nums if x > pivot]  # Bigger than pivot
        mid  =  [x for x in nums if x == pivot] # Equal to pivot
        right = [x for x in nums if x < pivot]  # Smaller than pivot
        
        # 2. Decide where 'k' lies
        
        # Case A: k is in the Left pile (The large numbers)
        if k <= len(left):
            return self.findKthLargest(left, k)
        
        # Case B: k is in the Mid pile (We found it!)
        # We check if k is covered by (Left + Mid)
        elif k <= len(left) + len(mid):
            return pivot
            
        # Case C: k must be in the Right pile
        # We skip over the Left and Mid piles, so we subtract their counts from k
        else:
            return self.findKthLargest(right, k - len(left) - len(mid))