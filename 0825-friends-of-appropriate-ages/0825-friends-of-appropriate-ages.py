class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1
            
        ans = 0
        # iterate 1 to 120. x and y represent the ages.
        for x, count_x in enumerate(count):
            for y, count_y in enumerate(count):
                
                # The conditions from the problem description
                if y <= 0.5 * x + 7: continue
                if y > x: continue
                if y > 100 and x < 100: continue
                
                # Add total possible connections between these two age groups
                ans += count_x * count_y
                
                # If ages are the same, remove self-requests
                if x == y:
                    ans -= count_x
                    
        return ans