class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        
        # 1. Precompute sums for every mask to speed up lookups
        # sum_for[mask] = sum of job times in that mask
        sum_for = [0] * (1 << n)
        for i in range(1 << n):
            current_sum = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_sum += jobs[j]
            sum_for[i] = current_sum

        # Memoization table
        memo = {}

        def dfs(mask, k_left):
            # Base Case: If only 1 worker left, they MUST take all remaining jobs
            if k_left == 1:
                return sum_for[mask]
            
            # Base Case: No jobs left, cost is 0
            if mask == 0:
                return 0
            
            state = (mask, k_left)
            if state in memo:
                return memo[state]
            
            res = float('inf')
            
            # ITERATE SUBMASKS: Try giving the current worker every possible subset of 'mask'
            # 'subset' starts as the full mask and we remove bits until we hit 0
            subset = mask
            while subset > 0:
                # 1. Current worker takes 'subset'
                current_load = sum_for[subset]
                
                # Optimization: If this single worker already exceeds our current best found in this loop,
                # there is no point checking the recursive branch (pruning).
                if current_load < res:
                    # 2. Remaining workers handle (mask ^ subset)
                    remaining_max = dfs(mask ^ subset, k_left - 1)
                    
                    # 3. The score for this split is the Max of (Current vs Others)
                    res = min(res, max(current_load, remaining_max))
                
                # Move to next subset (Bit trick)
                subset = (subset - 1) & mask
            
            memo[state] = res
            return res

        # Start with all jobs (mask 111...1) and k workers
        return dfs((1 << n) - 1, k)