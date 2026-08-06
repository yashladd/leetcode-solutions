class Solution:
    def check(self, nums: List[int]) -> bool:
        def rev(a, s, e):
            while s < e:
                a[s], a[e] = a[e], a[s]
                s += 1
                e -= 1
        N  = len(nums)
        for k in range(N):
            a = nums[:] # [3,4,5,1,2]
            rev(a, 0, N-1) # [2,1,5,4,3]
            rev(a, 0, k-1) #[1,2, 5,4,3]
            rev(a, k, N-1) #[1,2, 5,4,3]
            is_sorted = True
            for i in range(N-1):
                if a[i+1] < a[i]:
                    is_sorted = False
                    break

            if is_sorted:
                return True

        return False

            

            