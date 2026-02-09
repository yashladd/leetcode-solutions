class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income <= 0: 
            return 0

        n = len(brackets)
        tax = 0
        previousBracket = 0
        for i in range(n):
            currentBracket, percent = brackets[i]
            taxableIncome = min(income , currentBracket) - previousBracket
            tax += taxableIncome * percent / 100
            if currentBracket >= income:
                # print('reacehc')
                return tax
            previousBracket = currentBracket
            

        return tax