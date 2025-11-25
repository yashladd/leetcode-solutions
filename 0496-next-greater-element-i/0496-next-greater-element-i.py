class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = { x:i for i, x in enumerate(nums1) }
        res = [-1 for x in nums1]
        stk = []

        for i in range(len(nums2)-1, -1, -1):
            while stk and stk[-1] <= nums2[i]:
                stk.pop()
            if stk and nums2[i] in h:
                res[h[nums2[i]]] = stk[-1]
            stk.append(nums2[i])

        # for i, x in enumerate(nums2):
        #     while stk and stk[-1] < x:
        #         y = stk.pop()
        #         if y in h:
        #             res[h[y]] = x
        #     stk.append(x)
        return res 
        