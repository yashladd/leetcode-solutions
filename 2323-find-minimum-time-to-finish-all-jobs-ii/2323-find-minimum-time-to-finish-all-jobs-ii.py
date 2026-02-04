class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        return max(int(ceil(j/w)) for j, w in zip(sorted(jobs), sorted(workers)))