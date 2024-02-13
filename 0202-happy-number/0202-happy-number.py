class Solution:
    def isHappy(self, n: int) -> bool:
        def squared(n):
            result = 0
            while n>0:
                last = n%10
                result += last * last
                n = n//10
            return result
        
        slow = squared(n)
        fast = squared(squared(n))

        while slow!=fast and fast!=1:
            slow = squared(slow)
            fast = squared(squared(fast))

        return fast==1