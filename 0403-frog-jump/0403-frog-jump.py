class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        
        # Quick check: The first jump must be exactly 1 unit to stone[1]
        if stones[1] != 1:
            return False
            
        # Map stone value to its index for O(1) lookups
        stone_map = {val: i for i, val in enumerate(stones)}
        
        @cache
        def f(i, p):
            if i == n - 1:
                return True
            
            # The frog can jump k-1, k, or k+1 units
            for jump in [p - 1, p, p + 1]:
                if jump <= 0:
                    continue
                
                next_stone_val = stones[i] + jump
                
                # Check if a stone exists at the calculated position
                if next_stone_val in stone_map:
                    if f(stone_map[next_stone_val], jump):
                        return True
            
            return False
        
        # Start at index 1 (the second stone) because we already 
        # confirmed the first jump of 1 unit was successful.
        return f(1, 1)