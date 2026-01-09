class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        
        # Initialize 2D array with 0 (representing uncalculated states)
        # Rows: current_len (1 to n), Cols: paste_len (0 to n)
        self.memo = [[0] * (n + 1) for _ in range(n + 1)]
        self.n = n
        
        # Start: current_len = 1, paste_len = 1 (after first copy)
        # We add 1 to the result for that initial "Copy All" operation
        return 1 + self.dfs(1, 1)

    def dfs(self, l, c):
        if l == self.n:
            return 0
        if l > self.n:
            return 1000 # Max value/Invalid path
        
        # Check 2D array instead of dict
        if self.memo[l][c] != 0:
            return self.memo[l][c]
            
        # Logic: 
        # Option 1: Paste (1 op) -> new length is l + c, clipboard stays c
        res_paste = 1 + self.dfs(l + c, c)
        
        # Option 2: Copy All + Paste (2 ops) -> new length is l * 2, clipboard becomes l
        res_copy_paste = 2 + self.dfs(l * 2, l)
        
        # Store result in array
        self.memo[l][c] = min(res_paste, res_copy_paste)
        return self.memo[l][c]