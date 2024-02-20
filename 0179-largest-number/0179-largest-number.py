class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # NOTICE -1 if greater since we want to sort descending
        def cmp(x, y):
            return -1 if x + y >= y + x else 1
        
        a = sorted(map(str, nums), key=cmp_to_key(cmp))
        return "0" if a[0] == "0" else "".join(a)
        
        
        
        