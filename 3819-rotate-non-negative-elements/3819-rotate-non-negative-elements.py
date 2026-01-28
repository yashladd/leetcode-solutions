class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        """
        0 2 4
        
        3


        """

        posIdxs = set()
        values = []
        for i, n in enumerate(nums):
            if n >= 0:
                posIdxs.add(i)
                values.append(n)
        if not values:
            return nums
            
        k = k % len(values)
        print(values, k)
        def rev(a, s, e):
            while s < e:
                a[s], a[e] = a[e], a[s]
                s += 1
                e -= 1

        rev(values, 0, k-1)
        rev(values, k, len(values)-1)
        rev(values, 0, len(values)-1)
        print(values)
        for i in range(len(nums)):
            if i in posIdxs:
                nums[i] = values.pop(0)

        return nums
        