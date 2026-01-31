class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        # prefix = [nums[0]]
        
        # for i in range(1, len(nums)):
        #     prefix.append(prefix[i-1]+nums[i])
            
        # out = []
        # for i in range(len(nums)):
        #     if i<k or i>=len(nums)-k:
        #         out.append(-1)
        #     else:
        #         out.append(int((prefix[i+k]-prefix[i-k]+nums[i-k])/(2*k+1)))
        # return out
        prefix = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        
        out = []
        for i in range(len(nums)):

            if i<k or i>=len(nums)-k:
                out.append(-1)
            else:
                s = prefix[1+i+k] - prefix[i-k]
                out.append(s//(2*k + 1))
        return out


