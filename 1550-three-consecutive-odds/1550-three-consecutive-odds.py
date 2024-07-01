class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        j = 0   
        
        n = len(arr)
        
        while i < n:
            j = i
            while j < n and arr[j] % 2:
                j += 1
                
            if j - i >= 3:
                return True
            
            i = max(i+1, j)
            
        return False