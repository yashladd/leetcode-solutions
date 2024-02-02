class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(a, s, e):
            while s < e:
                a[s], a[e] = a[e], a[s]
                s += 1
                e -= 1
        k = k % (len(nums))
        rev(nums, 0, len(nums)-1)
        rev(nums, 0, k-1)
        rev(nums, k, len(nums)-1)