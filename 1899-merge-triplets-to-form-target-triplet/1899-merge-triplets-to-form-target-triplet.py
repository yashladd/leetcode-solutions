class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        at, bt, ct = target
        cnt = 0
        for i in range(len(triplets)):
            a, b, c = triplets[i]
            if a > at or b > bt or c > ct:
                continue
                
            for i, v in enumerate(triplets[i]):
                if v == target[i]:
                    found.add(i)
    
        return len(found) == 3
        
            
            
        if at not in h0 or bt not in h1 or ct not in h2:
            return False
        
        for triplet in triplets:
            if triplet == target:
                return True
            a, b, c = triplet
            idx1 = h0[at]
            idx2 = h1[bt]
            idx3 = h2[ct]
            if len(set([idx1, idx2, idx3])) == 3:
                return False
            i1, i2 = list(set([idx1, idx2, idx3]))
            a1, b1, c1 = max(triplets[i1][0], triplets[i2][0]), max(triplets[i1][1], triplets[i2][1]), max(triplets[i1][2], triplets[i2][2])
            if a1 == at and b1 == bt and c1 == ct:
                return True
            
        return False