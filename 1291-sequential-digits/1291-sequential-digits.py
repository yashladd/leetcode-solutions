class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n1, n2 = len(str(low)), len(str(high))
        res = set()

        def createNum(start, n):
            num = 0
            while n:
                if start == 10:
                    return num
                num = (num * 10) + start
                start += 1
                n-=1
            return num

        n = n1
        while n <= n2:
            tmp = []
            for startDigit in range(1, 10):
                num = createNum(startDigit, n)
                if num >= low and num <=high:
                    res.add(num)
                else:
                    continue
            n += 1
        return sorted(list(res))

        