import bisect

class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        valid_pairs = []
        
        # Step 1: Filter valid elements and create (X, Y) pairs
        for i, num in enumerate(nums):
            if num <= i:
                # X = num (value/target index), Y = i - num (required shifts)
                valid_pairs.append((num, i - num))
                
        if not valid_pairs:
            return 0
            
        # Step 2: Sort by X ascending, then by Y descending
        valid_pairs.sort(key=lambda pair: (pair[0], -pair[1]))
        
        # Step 3: Find Longest Non-Decreasing Subsequence on Y
        tails = []
        for x, y in valid_pairs:
            # We use bisect_right because we want a non-decreasing subsequence (y1 <= y2)
            idx = bisect.bisect_right(tails, y)
            
            if idx == len(tails):
                tails.append(y)
            else:
                tails[idx] = y
                
        return len(tails)