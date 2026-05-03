class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [-1] * n
        nums = nums + nums
        stk = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            while stk and nums[i] >= stk[-1]:
                stk.pop()

            if i < n:
                if stk:
                    out[i] = stk[-1]
            
            stk.append(nums[i])

        return out
            

                

