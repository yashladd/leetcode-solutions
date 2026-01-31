class Solution:
    def nextGreatestLetter(self, a: List[str], t: str) -> str:
        """

        
        """
        l = 0
        r = len(a)-1
        res = a[0]
        while l <= r:
            m = (l + r) >> 1

            if a[m] > t:
                res = a[m]
                r = m - 1
            else:
                l = m + 1

        return res

