class Solution:
    def minMoves(self, b: List[int]) -> int:
        """
        6 -1 -10 3 1 1
        10 + 3 + 2  + 4
        """
        negIdx = None
        n = len(b)
        for i in range(n):
            if b[i] < 0:
                negIdx = i
                break
        if negIdx is None:
            return 0
        left = (negIdx - 1) % n
        leftD = 1
        
        right = (negIdx + 1) % n
        rightD = 1
        val = abs(b[negIdx])
        otherSum = sum(b[:negIdx] + b[negIdx+1:])
        if otherSum < val:
            return -1
        mini = 0
        dis = 1
        while val > 0:
            while b[left] <= 0:
                left = (left - 1) % n
                leftD += 1 

            while b[right] <= 0:
                right = (right + 1) % n
                rightD += 1

            if leftD <= rightD:
                take = b[left] if b[left] <= val else val
                val = max(0, val - b[left])
                mini += (leftD * take)
                left = (left - 1) % n
                leftD += 1
            else:
                take = b[right] if b[right] <= val else val
                val = max(0, val - b[right])
                mini += (rightD * take)
                right = (right + 1) % n
                rightD += 1

        return mini

