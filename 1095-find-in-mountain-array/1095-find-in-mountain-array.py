class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # 1. FIND PEAK INDEX
        l, r = 0, n - 1
        while l < r:
            m = (l + r) >> 1
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m + 1
            else:
                r = m
        peakIdx = l
        
        # 2. SEARCH LEFT (Strictly Increasing)
        l, r = 0, peakIdx
        while l <= r:
            m = (l + r) >> 1
            val = mountain_arr.get(m) # Call once!
            
            if val == target:
                return m
            elif val < target:
                l = m + 1  # Move Right
            else:
                r = m - 1  # Move Left
        
        # 3. SEARCH RIGHT (Strictly Decreasing)
        l, r = peakIdx, n - 1
        while l <= r:
            m = (l + r) >> 1
            val = mountain_arr.get(m) # Call once!
            
            if val == target:
                return m
            elif val > target: # NOTE: Logic flipped for decreasing array
                l = m + 1  # Move Right (towards smaller values)
            else:
                r = m - 1  # Move Left (towards larger values)
                
        return -1