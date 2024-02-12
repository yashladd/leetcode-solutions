class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        s = set(arr)
        for i in range(1, len(arr) + k + 1):
            if i not in s:
                k -= 1
            if k == 0:
                return i
        return n
                
    
    
    