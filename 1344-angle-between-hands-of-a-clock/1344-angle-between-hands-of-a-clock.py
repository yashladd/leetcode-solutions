class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        min 5mins  = 30 
        1 min = 6
        
        hr = (hr % 12) x 30  + .5 x mins
        
        60 mins hr moves 30 
        1 min move extra .5 x 30 = 15 
        
        180 - 15
        
        
        6 x 30 = 180
        
        3 x 30 + .5 x 15 = 97.5
        
        
        
        """
        
        
        hr_move_per_hr = 30
        min_move_per_min = 6
        
        hr_extra_per_min = 0.5
        
        
        hr_pos_from_zero = (hour % 12) * hr_move_per_hr + minutes * hr_extra_per_min 
        
        min_pos_from_zero = minutes * min_move_per_min
        
        
        angle = abs(min_pos_from_zero - hr_pos_from_zero)
        otherAngle = 360 - angle
        
        return min(angle, otherAngle)