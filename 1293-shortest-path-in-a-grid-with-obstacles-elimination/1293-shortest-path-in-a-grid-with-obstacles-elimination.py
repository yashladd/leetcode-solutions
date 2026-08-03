class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        if k >= n + m:
            return n + m - 2


        if grid[0][0] == 1 and k == 0:
            return -1


        vis = [[(k  + 1)for _ in range(m)] for _ in range(n)]
        need_remove_start = (grid[0][0] == 1)
        q = deque([(0, 0, need_remove_start, 0)])

        vis[0][0] = need_remove_start


        while q:
            row, col, removals, steps = q.popleft()

            if row == n-1 and col == m-1:
                return steps

            for dx, dy in dirs:
                next_row, next_col = row + dx, col + dy
                if next_row < n and next_col < m and next_row >= 0 and next_col >= 0:
                    need_remove_cell = (grid[next_row][next_col] == 1)
                    new_removals = removals + need_remove_cell
                    if vis[next_row][next_col] > new_removals:
                        vis[next_row][next_col] = new_removals
                        q.append((next_row, next_col, new_removals, steps + 1))


        return -1

        
