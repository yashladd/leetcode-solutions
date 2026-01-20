class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 1, n-2
        while l <= r:
            m = (l + r) >> 1

            if (arr[m-1] < arr[m] and arr[m] > arr[m+1]):
                return m
            elif arr[m + 1] > arr[m]:
                l = m + 1
            else:
                r = m - 1 



        return -1 