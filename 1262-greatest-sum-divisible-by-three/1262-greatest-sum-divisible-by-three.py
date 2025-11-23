class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float("inf")
        
        # 1. Pre-allocate TWO lists
        prev = [0, -INF, -INF]
        curr = [-INF, -INF, -INF] 
        
        for x in nums:
            # (Note: You must overwrite ALL indices of curr, 
            # because curr now holds 'dirty' data from 2 steps ago)
            
            for m in range(3):
                # Calculate values using 'prev' and write into 'curr'
                # ... (your logic here) ...
                # Example logic:
                curr[m] = max(prev[m], prev[(m - x) % 3] + x)
            
            # 2. SWAP the references
            # This is instant. 'prev' now points to the list that was 'curr'
            # 'curr' points to the old 'prev' (which we will overwrite next loop)
            prev, curr = curr, prev
            
        return prev[0]