class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)
        maxSubSum = nums[0]
        currSum = nums[0]

        for i in range(1, n):
            currSum = max(currSum + nums[i], nums[i])
            maxSubSum = max(currSum, maxSubSum)

        print("Before", maxSubSum)
        
        currSum = nums[0]
        minSubSum = nums[0]

        for i in range(1, n-1):
            currSum = min(currSum + nums[i], nums[i])
            minSubSum = min(currSum, minSubSum)
            # print(currSum, minSubSum)
            maxSubSum = max(maxSubSum, totalSum - minSubSum)


        return maxSubSum

        