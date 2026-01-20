class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # ---------------------------------------------------------
        # STEP 1: FIND PEAK (Using YOUR Logic)
        # ---------------------------------------------------------
        l, r = 1, n - 2
        peak_idx = -1
        
        while l <= r:
            m = (l + r) >> 1
            
            # We cache the values to save API calls (limit is 100)
            val = mountain_arr.get(m)
            val_left = mountain_arr.get(m - 1)
            val_right = mountain_arr.get(m + 1)
            
            # 1. Found the Peak?
            if val_left < val and val > val_right:
                peak_idx = m
                break
            
            if val < val_right:
                l = m + 1
            
            # 3. Descending Slope? (Move Left)
            # Your logic: r = m.
            # Optimization: r = m - 1 is safer and faster
            else:
                r = m - 1
                
        # ---------------------------------------------------------
        # STEP 2: SEARCH LEFT (Ascending part: 0 to peak)
        # ---------------------------------------------------------
        l, r = 0, peak_idx
        while l <= r:
            m = (l + r) >> 1
            val = mountain_arr.get(m)
            
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1
                
        # ---------------------------------------------------------
        # STEP 3: SEARCH RIGHT (Descending part: peak to n-1)
        # ---------------------------------------------------------
        l, r = peak_idx, n - 1
        while l <= r:
            m = (l + r) >> 1
            val = mountain_arr.get(m)
            
            if val == target:
                return m
            elif val > target:  # NOTE: Logic is reversed for descending side!
                l = m + 1       # If val > target, we need smaller, so go Right
            else:
                r = m - 1
                
        return -1