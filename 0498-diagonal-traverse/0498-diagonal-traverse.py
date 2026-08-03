from collections import defaultdict
from typing import List

"""

Let's break down exactly how we get m + n - 1:

1. The First Diagonal (Minimum Sum)
The very first element in any matrix is at the top-left corner.

Row index (r): 0

Col index (c): 0

Diagonal Index (r + c): 0 + 0 = 0

So, our diagonals always start at 0.

2. The Last Diagonal (Maximum Sum)
The very last element in the matrix is at the bottom-right corner.

Max Row index (r): m - 1 (since arrays are 0-indexed)

Max Col index (c): n - 1

Diagonal Index (r + c): (m - 1) + (n - 1) = m + n - 2

So, our highest possible diagonal index is m + n - 2.
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Group elements by the sum of their indices (r + c)
        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
                
        res = []
        
        # The sum of indices ranges from 0 to (m - 1) + (n - 1)
        for d in range(m + n - 1):
            # Even diagonals traverse UP, so we reverse the naturally DOWN order
            if d % 2 == 0:
                res.extend(diagonals[d][::-1])
            # Odd diagonals traverse DOWN, so we append them as they are
            else:
                res.extend(diagonals[d])
                
        return res