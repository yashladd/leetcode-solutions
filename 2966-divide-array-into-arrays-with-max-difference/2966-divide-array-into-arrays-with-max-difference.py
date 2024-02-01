class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            tmp = nums[i:i+3]
            if tmp[2] - tmp[0] > k:
                return []
            res.append(tmp)

        return res





        