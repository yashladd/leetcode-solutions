class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        [3 8 1 2 9 5 7] k = 3
        [1 2 3 5 7 8 9]
         0 1 2 3 4 5 6
        n = 7
        """

        a = sorted(nums)

        n = len(a)
        mini = float("inf")
        for i in range(n-k+1):
            mini = min(mini, a[i + k -1] - a[i])

        return mini

        