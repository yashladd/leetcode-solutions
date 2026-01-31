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
        
        max_ = i + 1
			# max number greater on right that less than A[i]
        for j in range(max_ + 1, len(arr)):
            if arr[max_] < arr[j] < arr[i]: 
                max_ = j
            
        
        
        arr[i], arr[max_] = arr[max_], arr[i]
        
        return arr
        
        
        
        
        
        
        
        