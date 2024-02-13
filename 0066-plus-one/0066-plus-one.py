class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        c = 0
        for i in reversed(range(len(digits))):
            cur = digits[i]
            if i == len(digits) - 1:
                cur += 1
            cur += c
            res.append(cur%10)
            c = cur // 10
        if c:
            res.append(c)
        return res[::-1]
            
            
            
        