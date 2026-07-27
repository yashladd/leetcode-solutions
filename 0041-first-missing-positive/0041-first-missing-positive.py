class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Finds the smallest positive integer that is missing from an unsorted array.
        
        This algorithm runs in O(n) time and uses O(1) auxiliary space by using the 
        input array itself as a hash map. It "fingerprints" the presence of a number 
        `x` by turning the value at index `x - 1` into a negative number.

        Args:
            nums (list[int]): An unsorted array of integers.

        Returns:
            int: The smallest missing positive integer.

        Examples:
            Example 1: nums = [3, 4, -1, 1]
            
            Step 1: Sanitize array (turn negatives to 0)
                    State: [3, 4, 0, 1]
                    
            Step 2: Fingerprint occurrences (mark indices as visited)
                    - i=0, value=3: index 2 becomes negative -> [3, 4, -5, 1] (0 replaced with out-of-bounds negative)
                    - i=1, value=4: index 3 becomes negative -> [3, 4, -5, -1]
                    - i=2, value=5: ignore (out of bounds)
                    - i=3, value=1: index 0 becomes negative -> [-3, 4, -5, -1]
                    Final State: [-3, 4, -5, -1]
                    
            Step 3: Find first missing
                    - Index 0 is -3 (visited, meaning 1 exists)
                    - Index 1 is 4  (NOT visited, meaning 2 is missing) -> Return 2!
        """
        n = len(nums)

        # Step 1: Sanitize the array. 
        # Negative numbers are irrelevant to finding the first missing positive,
        # so we convert them to 0 to prepare the array for the fingerprinting phase.
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # Step 2: Fingerprint the array.
        # Use the index of the array to record the presence of a number.
        for i in range(n):
            value = abs(nums[i])
            
            # We only care about numbers that can validly map to our array indices [1, n]
            if 1 <= value <= n:
                target_index = value - 1
                
                # Mark as visited by turning the value at target_index negative.
                if nums[target_index] > 0:
                    nums[target_index] *= -1
                
                # If the value is 0, we can't multiply by -1. 
                # Instead, replace it with a negative number safely outside our range [1, n].
                elif nums[target_index] == 0:
                    nums[target_index] = -(n + 1)

        # Step 3: Identify the missing positive.
        # The first index that holds a non-negative number corresponds to our missing integer.
        for i in range(n):
            if nums[i] >= 0:
                # Indices are 0-based, but our positive numbers are 1-based.
                return i + 1
        
        # If all indices from 0 to n-1 were marked negative, it means the array 
        # contained a perfect sequence from 1 to n. The next missing number is n + 1.
        return n + 1