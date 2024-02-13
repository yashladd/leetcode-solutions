class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        curr = n
        res = 0
        while True:
            res = 0
            while curr:
                res += (curr%10) ** 2
                curr = curr//10
            if res == 1:
                return True
            if res in s:
                break
            else:
                s.add(res)
            curr = res

        return False

        