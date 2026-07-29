class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = min(weights)
        high = sum(weights)

        min_capacity = high


        def can_ship(capacity, max_days):
            days = 1
            curr_load = 0
            for i, weight in enumerate(weights):
                if weight > capacity:
                    return False
                if days > max_days:
                    return False
                curr_load += weight
                if curr_load > capacity:
                    curr_load = weight
                    days += 1
                    
            return days <= max_days
                

        while low <= high:
            mid = (low + high) >> 1

            if can_ship(mid, days):
                min_capacity = mid
                high = mid - 1
            else:
                low = mid + 1


        return min_capacity


