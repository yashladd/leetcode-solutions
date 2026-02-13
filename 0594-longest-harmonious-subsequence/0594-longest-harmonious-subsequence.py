from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Step 1: Count frequencies of all numbers - O(n)
        counts = Counter(nums)
        max_length = 0
        
        # Step 2: Iterate through the unique numbers - O(n)
        for x in counts:
            # Check if the "harmonious partner" (x + 1) exists
            if x + 1 in counts:
                # The total length is the sum of their frequencies
                max_length = max(max_length, counts[x] + counts[x+1])
        
        return max_length