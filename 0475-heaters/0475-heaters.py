class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
         0  1  2  3    4  5
        [1, 4, 6, 10, 11, 30]
        heaters = [3, 7, 15]
        """
        houses.sort()
        heaters.sort()
        lo = 0
        hi = 10**9
        res = hi

        def canMake(radius):
            h_idx = 0  # Pointer for houses
            
            for heater in heaters:
                # Define the range covered by this heater
                left_limit = heater - radius
                right_limit = heater + radius
                
                # Advance the house pointer if the house is covered by this heater
                while h_idx < len(houses) and left_limit <= houses[h_idx] <= right_limit:
                    h_idx += 1
                    
                # Optimization: If all houses are covered, we can stop early
                if h_idx == len(houses):
                    return True
                    
            # If we finished checking all heaters but still have houses left
            return h_idx == len(houses)


        while lo <= hi:
            mid = (lo + hi) >> 1

            if canMake(mid):
                res = mid
                hi = mid-1
            else:
                lo = mid + 1

        return res
