class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        A = [0] * (amount + 1)
        A[0] = 1
        
        for i in range(len(coins)):
            for j in range(1,amount+1):
                if coins[i] <= j:
                    A[j] = A[j] + A[j-coins[i]]
                    
        return A[-1]
        