class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(a) - 1
        
        while l < r:
            for i in range(r-l):
                top, bot = l, r
                #Store top left
                tl = a[top][l + i]
                # Move bl -> tl
                a[top][l + i] = a[bot - i][l]
                #Move br -> bl
                a[bot - i][l] = a[bot][r -i]
                # move tr -> br
                a[bot][r-i] = a[top+i][r]
                # Finally move tl => tr
                a[top+i][r] = tl
                
            l+=1
            r-=1
            
            
                