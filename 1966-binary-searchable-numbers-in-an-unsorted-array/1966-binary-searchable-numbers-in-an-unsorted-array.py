class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n  = len(nums)
        INF = float("inf")

        can_search = [True] * n

        max_so_far = -INF

        for i, x in enumerate(nums):
            if x < max_so_far:
                can_search[i] = False
            else:
                max_so_far = x

        min_so_far = INF

        for i in range(n-1, -1, -1):
            x = nums[i]
            if x > min_so_far:
                can_search[i] = False
            else:
                min_so_far = x


        return sum(can_search)
        