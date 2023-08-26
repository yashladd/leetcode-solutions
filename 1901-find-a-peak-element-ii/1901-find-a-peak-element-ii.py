class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        lo = 0
        hi = m-1
        while lo <= hi:
            midCol = (lo + hi) >> 1
            maxRow = 0
            for row in range(n):
                if mat[row][midCol] > mat[maxRow][midCol]:
                    maxRow = row
            
            upElement = mat[maxRow][midCol - 1] if midCol - 1 >= 0 else -1
            downElement = mat[maxRow][midCol + 1] if midCol  + 1 < m else -1
            if mat[maxRow][midCol] >= upElement and \
                    mat[maxRow][midCol] >= downElement:
                return [maxRow, midCol]
            elif upElement > mat[maxRow][midCol]:
                hi = midCol - 1
            else:
                lo = midCol + 1
                
        return [-1, -1]
        