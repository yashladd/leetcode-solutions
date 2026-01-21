class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)
        maxSubSum = nums[0]
        currSum = nums[0]
        # Maybe the ans in within the normal array not circular
        # Find this max sub aray sum using kadane's algo
        for i in range(1, n):
            currSum = max(currSum + nums[i], nums[i])
            maxSubSum = max(currSum, maxSubSum)
        
        currSum = nums[0]
        minSubSum = nums[0]

        # [ * *  ### * * * ]
        # If ### is minSum then total - sumof of this portion will give me the 
        # max sum excluding this portion the sircular portion represented by *
        # NOTE: only find minSum from [1, n-2] 
        # if we find for all array then circular can be total - total = 0
        # We want to take atleast 1 element in the subarry 

        for i in range(1, n-1):
            currSum = min(currSum + nums[i], nums[i])
            minSubSum = min(currSum, minSubSum)
            # print(currSum, minSubSum)
            maxSubSum = max(maxSubSum, totalSum - minSubSum)


        return maxSubSum

        