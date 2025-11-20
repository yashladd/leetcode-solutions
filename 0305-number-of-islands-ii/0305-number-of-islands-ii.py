class DS:
    def __init__(self, total_nodes):
        # Parent array
        self.p = [i for i in range(total_nodes)]
        # Rank/Size array (optional, but good for optimization)
        self.s = [1 for _ in range(total_nodes)]

    def find(self, u):
        if u == self.p[u]:
            return u
        # Path compression
        self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, u, v):
        # CRITICAL FIX: Find the ROOTs of u and v, not just immediate parents
        root_u = self.find(u)
        root_v = self.find(v)
        
        # If they are already in the same set, return False (no merge happened)
        if root_u == root_v:
            return False
        
        # Union by size/rank
        if self.s[root_u] < self.s[root_v]:
            self.p[root_u] = root_v
            self.s[root_v] += self.s[root_u]
        else:
            self.p[root_v] = root_u
            self.s[root_u] += self.s[root_v]
            
        # Return True to indicate a merge occurred
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ds = DS(m * n)
        isl = 0
        # Use a set for fast lookup of existing land
        grid_set = set()
        res = []
        
        for r, c in positions:
            # CRITICAL FIX: Mapping formula is r * n + c
            index = r * n + c
            
            # If this position is already land, the count doesn't change.
            # Just append current count and skip.
            if index in grid_set:
                res.append(isl)
                continue
                
            grid_set.add(index)
            isl += 1 # Assume it's a new isolated island first
            
            # Check 4 directions
            for dx, dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dx, c + dy
                
                if 0 <= nr < m and 0 <= nc < n:
                    neighbor_index = nr * n + nc
                    
                    # If neighbor is land, try to union
                    if neighbor_index in grid_set:
                        # CRITICAL FIX: Only decrement if they were actually separate islands
                        if ds.union(index, neighbor_index):
                            isl -= 1
            
            res.append(isl)
        
        return res