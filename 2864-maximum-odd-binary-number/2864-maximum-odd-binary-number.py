class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        h = Counter(s)
        res = "1" * ( h["1"] - 1) + "0" * (h["0"]) + "1"
        return res
        