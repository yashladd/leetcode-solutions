class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for val, romanNumeral in zip(values, numerals):
            if num == 0: break
            cnt, num = divmod(num, val)
            res += (cnt * romanNumeral)
        return res