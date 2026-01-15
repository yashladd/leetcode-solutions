class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """

        1 3 5
        x 9 9
          8 1

        """
        n1 , n2 = len(num1) , len(num2)
        if "0" in [num1, num2]: return "0"
        
        one, two = num1[::-1], num2[::-1]
        res = [0] * (n1 + n2)
        for i, c1 in enumerate(one):
            for j, c2 in enumerate(two):
                mul = int(c1) * int(c2)
                res[i + j] += mul
                res[i + j + 1] += (res[i + j] //10)
                res[i+j] %= 10
        return "".join(list(map(str, res[::-1]))).lstrip("0")

        