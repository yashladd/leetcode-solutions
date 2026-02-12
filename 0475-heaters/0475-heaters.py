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
            for house in houses:
                # Find the first heater to the right of the house
                idx = bisect_left(heaters, house)
                
                covered = False
                # Check heater to the right
                if idx < len(heaters) and heaters[idx] - radius <= house:
                    covered = True
                # Check heater to the left
                if not covered and idx > 0 and heaters[idx-1] + radius >= house:
                    covered = True
                    
                if not covered:
                    return False
            return True


        while lo <= hi:
            mid = (lo + hi) >> 1

            if canMake(mid):
                res = mid
                hi = mid-1
            else:
                lo = mid + 1

        return res
