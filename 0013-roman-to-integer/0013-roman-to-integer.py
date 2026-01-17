class Solution:
    def romanToInt(self, s: str) -> int:
        """
        V = 5, X=10, L=50, C=100, D=500, M=1000

        Range 1-9:
            # if first letter is I:
            1. check the next letter (V, X) for 4 & 9
            2. if not next could be upto 2 more II -> For this we can consider 
            values individually add their contribution

            # if first letter is V:
            1. Upto 3 I can follow
        
        Range 10-99:
        X XX XXX XL L LX LXX LXXX  XC
        Here also we notice that we only need to handle 
        XL 40 & 
        XC 90
        in a special case, the rest could be handled by considering 
        individual contribution of the letters:
        Xample 80 -> LXXX
        """
        
        romanDict = {
            "I": 1,
            "V": 5,
            "IV": 4,
            "X": 10,
            "IX": 9,
            "L": 50,
            "XL": 40,
            "C": 100,
            "XC": 90,
            "D": 500,
            "CD": 400,
            "M": 1000,
            "CM": 900 
        }

        integer = 0
        i = 0
        N = len(s)

        while i < N:
            if i + 2 <= N:
                roman = s[i: i + 2]
                if roman in romanDict:
                    integer += romanDict[roman]
                    i += 2
                    continue

            integer += romanDict[s[i]]

            i += 1

        return integer  