class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        res = []
        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)

        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])

        return res
        