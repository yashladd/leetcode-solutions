class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Find the midpoint
        # For odd lengths, the smaller half needs one extra element
        n = len(nums)
        mid = (n + 1) // 2
        
        # Step 3: Split into two halves
        small_half = nums[:mid]
        large_half = nums[mid:]
        
        # Step 4: Reverse both halves and assign to appropriate indices
        # Even indices (0, 2, 4...) get the smaller half (reversed)
        nums[::2] = small_half[::-1]
        
        # Odd indices (1, 3, 5...) get the larger half (reversed)
        nums[1::2] = large_half[::-1]