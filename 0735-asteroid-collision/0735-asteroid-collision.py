class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        """

        """
        i = 0
        res = []
        n = len(a)
        stk = []
        while i < n and a[i] < 0:
            res.append(a[i])
            i += 1

        for j in range(i, n):
            # Only collide if top of stack is Right (+) and current is Left (-)
            while stk and stk[-1] > 0 and a[j] < 0:
                prev = stk.pop()
                if prev == abs(a[j]):
                    break
                elif prev > abs(a[j]):
                    stk.append(prev)
                    break
            else:
                stk.append(a[j])

        return res + stk


        