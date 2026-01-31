class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        
        1 5 3 9 8
        15389??
        """
        
        n = len(arr)
        if n <= 1:
            return arr
        
        i = n-2
        
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
            
        if i < 0:
            return arr
        
        maxIdx = i+1
        maxNum = arr[maxIdx]
        for j in range(maxIdx+1, len(arr)):
            if arr[maxIdx] < arr[j] < arr[i]:
                maxNum = arr[j]
                maxIdx = j 
        
        
        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
        
        return arr
        
        
        
        
        
        
        
        