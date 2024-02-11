class Solution:
    def searchInsert(self, arr: List[int], x: int) -> int:
        return bisect.bisect_left(arr, x)