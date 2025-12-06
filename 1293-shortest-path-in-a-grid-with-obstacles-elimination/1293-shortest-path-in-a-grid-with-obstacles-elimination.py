from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Optimization: If k is large enough to walk the Manhattan distance 
        # (shortest path without walls), just return that distance immediately.
        # This prevents TLE/MLE on large grids with massive K.
        if k >= m + n - 2:
            return m + n - 2

        # State: (row, col, remaining_k)
        q = deque([(0, 0, k)])
        
        # Visited stores: visited[row][col] = max_k_remaining_seen_so_far
        # Initialize with -1 (meaning not visited yet)
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = k
        
        steps = 0
        
        while q:
            # Process level by level to track steps easily
            for _ in range(len(q)):
                r, c, rem = q.popleft()
                
                # Target reached
                if r == m - 1 and c == n - 1:
                    return steps
                
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = r + dx, c + dy
                    
                    if 0 <= nr < m and 0 <= nc < n:
                        # Calculate new remainder
                        new_rem = rem - grid[nr][nc]
                        
                        # LOGIC FIX:
                        # 1. Check if we have enough k (new_rem >= 0)
                        # 2. Check if this path is BETTER than previous paths to this cell
                        #    (new_rem > visited[nr][nc])
                        if new_rem >= 0 and new_rem > visited[nr][nc]:
                            visited[nr][nc] = new_rem
                            q.append((nr, nc, new_rem))
            
            steps += 1
            
        return -1