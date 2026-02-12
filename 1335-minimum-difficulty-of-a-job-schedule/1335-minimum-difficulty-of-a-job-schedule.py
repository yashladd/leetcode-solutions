class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def dp(jobs, d):
            A = [[float("inf")] * d for i in range(len(jobs))]
            A[0][0] = jobs[0]
            for i in range(1, len(jobs)):
                A[i][0] = max(A[i - 1][0], jobs[i])

            for i in range(1, len(jobs)):
                for j in range(1, min(i + 1, d)):
                    for k in range(i):
                        A[i][j] = min(A[i][j], A[k][j - 1] + max(jobs[k + 1:i + 1]))

            return A[-1][-1]
        ans = dp(jobDifficulty, d)
        return ans if ans != inf else -1