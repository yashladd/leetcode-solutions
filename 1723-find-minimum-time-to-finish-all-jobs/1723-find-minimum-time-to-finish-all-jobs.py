class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N = len(jobs)
        jobs.sort(reverse = True)
        min_max_load = sum(jobs)
        worker_load = [0] * k
        def back(job_idx):
            nonlocal min_max_load
            if  job_idx == N:
                min_max_load = min(min_max_load, max(worker_load))
                return 


            for worker_id in range(k):
                if worker_load[worker_id] + jobs[job_idx] >= min_max_load:
                    continue

                worker_load[worker_id] += jobs[job_idx]
                back(job_idx + 1)
                worker_load[worker_id] -= jobs[job_idx]

                if worker_load[worker_id] == 0:
                    break

        back(0)
        return min_max_load



