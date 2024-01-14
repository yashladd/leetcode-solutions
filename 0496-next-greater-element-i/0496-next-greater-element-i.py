class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {n:i for i, n in enumerate(nums1)}
        
        stk = []
        res = [-1] * len(nums1)
        
        for n in nums2:
            while stk and stk[-1] < n:
                num = stk.pop()
                pos = h[num]
                res[pos] = n
            if n in h:
                stk.append(n)
            
        return res
        