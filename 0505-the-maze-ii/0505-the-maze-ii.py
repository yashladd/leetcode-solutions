import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        dest_X, dest_Y = destination
        start_X, start_Y = start
        
        # 1. Use a distance array instead of a visited set
        dist = [[float('inf')] * m for _ in range(n)]
        dist[start_X][start_Y] = 0
        
        q = [(0, start_X, start_Y)]
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def inb(a, b):
            return 0 <= a < n and 0 <= b < m

        while q:
            curr_dis, x, y = heapq.heappop(q)
            
            # If we already found a better path to this node, skip processing
            
            
            if x == dest_X and y == dest_Y:
                return curr_dis

            if curr_dis > dist[x][y]:
                continue
            
            for dx, dy in DIRS:
                nx, ny = x, y
                count = 0
                
                # Roll until hitting a wall
                while inb(nx + dx, ny + dy) and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    count += 1
                
                # 2. Only push to heap if we found a strictly SHORTER path
                if dist[x][y] + count < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + count
                    heapq.heappush(q, (dist[nx][ny], nx, ny))
                    
        return -1 if dist[dest_X][dest_Y] == float('inf') else dist[dest_X][dest_Y]