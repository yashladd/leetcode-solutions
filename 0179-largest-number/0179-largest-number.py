class Cmp(str):
    def __lt__(x,y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # NOTICE -1 if greater since we want to sort descending
        def cmp(x, y):
            return -1 if x + y >= y + x else 1
        
        a = sorted(map(str, nums), key=Cmp)
        return str(int("".join(a)))
        
        
        
        