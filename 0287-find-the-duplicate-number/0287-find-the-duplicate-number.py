class Solution:
    def findDuplicate(self, a: List[int]) -> int:
        s = f = 0
        while True:
            s = a[s]
            f = a[a[f]]
            if s == f:
                break
                
        f = 0
        while s != f:
            s = a[s]
            f = a[f]
        return s
            