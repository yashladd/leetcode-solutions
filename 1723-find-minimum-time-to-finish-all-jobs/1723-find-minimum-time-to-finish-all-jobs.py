class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # Sort descending to fail fast
        jobs.sort(reverse=True)
        worker_loads = [0] * k
        self.res = sum(jobs) # Initial upper bound

        def backtrack(job_idx):
            # Base case: All jobs assigned
            if job_idx == len(jobs):
                self.res = min(self.res, max(worker_loads))
                return

            for i in range(k):
                # Pruning: If this path is already worse than our best, skip
                if worker_loads[i] + jobs[job_idx] >= self.res:
                    continue
                
                # Assign job
                worker_loads[i] += jobs[job_idx]
                backtrack(job_idx + 1)
                # Backtrack
                worker_loads[i] -= jobs[job_idx]

                # Optimization: If worker was empty, don't try next empty workers
                # This avoids redundant permutations.
                if worker_loads[i] == 0:
                    break

        backtrack(0)
        return self.res