class Solution:
    def maxA(self, n: int) -> int:
        @cache
        def solve(rem_ops):
            # Base Case: With 3 or fewer ops, max is just typing 'A' repeatedly
            # 1->1, 2->2, 3->3
            if rem_ops <= 3:
                return rem_ops
            
            # Option 1: Just type 'A' (simple addition)
            res = solve(rem_ops - 1) + 1
            
            # Option 2: Try every possible "Copy-Paste" multiplier sequence.
            # We need at least 3 moves to multiply (Select, Copy, Paste) => x2
            # We loop 'moves' representing the cost of (Select + Copy + Paste...Paste)
            # We stop at rem_ops - 1 because we need at least 1 op to create the initial 'A's
            for moves in range(3, rem_ops):
                # The multiplier is (moves - 1)
                # Example: 3 moves (Sel, Cop, Pas) = x2
                #          4 moves (Sel, Cop, Pas, Pas) = x3
                curr = solve(rem_ops - moves) * (moves - 1)
                res = max(res, curr)
            
            return res

        return solve(n)