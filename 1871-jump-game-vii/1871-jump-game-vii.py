from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Quick edge case: if the last character is '1', we can never land on it.
        if s[-1] == '1':
            return False
            
        n = len(s)
        queue = deque([0])
        farthest_reached = 0
        
        while queue:
            curr = queue.popleft()
            
            # The start of our next search window is either the minimum jump distance,
            # OR just past the farthest point we've already evaluated in previous steps.
            start = max(curr + minJump, farthest_reached + 1)
            end = min(curr + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)
                    
            # Update the watermark so we don't scan this range again
            farthest_reached = max(farthest_reached, end)
            
        return False