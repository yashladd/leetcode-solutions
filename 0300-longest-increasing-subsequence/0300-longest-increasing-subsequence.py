class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = []
        lis.append(nums[0])
        for i in range(1, n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                idx = bisect.bisect_left(lis, nums[i], 0, len(lis))
                lis[idx] = nums[i]
        return len(lis)
            