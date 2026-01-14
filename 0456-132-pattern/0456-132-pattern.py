class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        
        for n in nums:
            # print(stk)
            mini = n
            while stk and stk[-1][0] < n:
                mini = min(mini, stk[-1][1])
                stk.pop()
            # print("stk2", stk)
            if stk and stk[-1][0] > n and stk[-1][1] < n:
                return True
            stk.append([n, mini])
        return False