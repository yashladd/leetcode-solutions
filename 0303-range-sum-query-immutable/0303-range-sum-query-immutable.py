class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        

    def sumRange(self, left: int, right: int) -> int:
        s = 0
        l, r = left, right
        while l < r:
            s += self.a[l]
            s += self.a[r]
            l += 1
            r -= 1
        if not (left + right) % 2:
            s += self.a[r]
        return s
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)